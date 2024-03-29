from django.shortcuts import render, redirect

from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

from django import forms

import re

from markdown2 import Markdown
markdowner = Markdown()

import random



# Create your views here.

class NewSearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))


class NewCreateForm(forms.Form):
    title = forms.CharField(label="Title:", widget=forms.TextInput(attrs={'class': 'form-control w-75 mb-2'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))



def index(request):
    form = NewSearchForm()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'form': form
    })

def entry(request, title):
    entries = util.list_entries()
    form = NewSearchForm()
    title = title
    
    return render(request, "encyclopedia/entry.html", {
        "entries": util.get_entry(title),
        "form": form, 
        "title": title
    })

def search(request):

    val = request.GET['q']

    content = util.get_entry(val)

    if content:
        return HttpResponseRedirect(reverse('encyclopedia:entry', args=[val]))
    else:
        entries = util.list_entries()
        subStringEntries = []
        string = re.compile("(?i)(" + val + ")")      # ? Exist or Not 0|1   i# A case insensitive match is performed, meaning capital letters will be matched by non-capital letters and vice versa.
       
        for entry in entries:
            if string.search(entry):
                subStringEntries.append(entry)

        return render(request, "encyclopedia/search.html", {
            "string": val, 
            "subStringEntries": subStringEntries
            })


def topics(request):
    if request.method == "POST":
        # print(request.POST.get('entry'))
        form = NewCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            markdown = form.cleaned_data["content"]
            if util.get_entry(title):
                return render(request, "encyclopedia/error.html", {
                    "form": form,
                    "exists": True,
                    "title": title
                })
            else:
                # entry = form.cleaned_data["entry"]
                # print(entry)
                util.save_entry(title, markdown)
                return redirect('encyclopedia:index')
    else:
            # return render(request, "wiki/topics.html", {
            #     "form": form,
            #     "exists": False
            # })
        return render(request, "encyclopedia/topics.html", {
        "form": NewCreateForm(),
        "exists": False
    })




# 
# 

class ModifyForm(forms.Form):
     body = forms.CharField(label="Modify Body", widget=forms.Textarea(
        attrs={'class': 'form-control', 'cols': '10'}))
    
    
def modify(request, title):
    edform = ModifyForm(initial={'body': util.get_entry(title)})
    if request.method == "POST":
        modifyform = ModifyForm(request.POST)
        if modifyform.is_valid():
            # title = modifyform.cleaned_data.get("title")
            # newcontent = modifyform.cleaned_data.get("body")
            newcontent = modifyform.cleaned_data["body"]
            # saving the new content
            util.save_entry(title, newcontent)
            # form = NewSearchForm()
            # htmlcontent = markdowner.convert(newcontent)
            # return render(request, "wiki/modify.html", {
            #     "title": title, "content": htmlcontent, "form": form
            # })
            # return redirect(request, "wiki:index", {
            #     "title": title, "newcontent": htmlcontent
            # })
            return HttpResponseRedirect(reverse('encyclopedia:entry', args=[title]))
    else:
        # form = NewSearchForm()
        # modifyform = ModifyForm({"title": title, "newcontent": util.get_entry(title)})
        # return render(request, "wiki/modify.html", {"form": form, "modifyform": modifyform})
        # return redirect(request, "wiki:page", {"form": form, "modifyform": modifyform})
        # return render(request, "wiki/modify.html", {"title": title, "newcontent": util.get_entry(title)})
        return render(request, "encyclopedia/modify.html", {"title": title, "edform":edform})
    

def randoms(request):
    entries = util.list_entries()
    num = len(entries)
    # generating a random number for the entry
    entry = random.randint(0, num-1)
    title = entries[entry]
    mdcontent = util.get_entry(title)
    htmlcontent = markdowner.convert(mdcontent)
    form = NewSearchForm()
    return render(request, "encyclopedia/randoms.html", {"form": form, "title": title, "content": htmlcontent})

