from django.shortcuts import render
from . import util


# Create your views here.

def index(request):
    
    return render(request, "wiki/index.html", {
        "entries": util.list_entries()
        
        
    })

def page(request, title):
   
    return render(request, "wiki/page.html", {
        "entries": util.get_entry(title)
        
    })

def edit(request):
    return render(request, "wiki/edit.html") 