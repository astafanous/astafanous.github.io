
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect,  JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from .models import User, Post, Comment, Category, Page

from django.forms import ModelForm
from django import forms

import json

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required


from django.contrib import messages



class newPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'imageUrl', 'body', 'author', 'category']
        widgets = {
            'body': forms.Textarea(attrs={'id': 'id_body',
                                          'rows': 20,
                                          'maxlength': 1000,
                                          'class': 'form-control',
                                          'placeholder': 'Type your content'
                                          })
        }


class newPageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'imageUrl', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'id': 'id_content',
                                             'rows': 20,
                                             'maxlength': 1000,
                                             'class': 'form-control',
                                             'placeholder': 'Type your content'
                                             })
        }


@login_required
def create_post(request):
    if request.method == "POST":
        form = newPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")

            return HttpResponseRedirect(reverse("index"))
        else:
            print(form.errors)
            return render(request, "mysite/create.html", {
                "form": form,
                "message": "The form is invalid. Please resumbit"

            })
    else:
        return render(request, "mysite/create.html", {
            "form": newPostForm(),


        })


def index(request):
    posts = Post.objects.all().order_by("-id")
    profile_id = request.user.id if request.user.is_authenticated else None

    p = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page = p.get_page(page_number)
    return render(request, "mysite/index.html", {
        'posts': posts,
        'profile_id': profile_id,
        "page": page,

    })

@login_required
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(user=user).order_by("-id")
    return JsonResponse({'user_id': user_id, 'posts': posts, 'status': 'ok'})


@login_required
def page_home(request):

    latest_posts = Post.objects.order_by('-date')[:2]

    return render(request, "mysite/page_home.html", {'latest_posts': latest_posts})


def all_posts(request):
    posts = Post.objects.all().order_by("-id")

    return render(request, "mysite/all_posts.html", {
        "posts": posts,
        "form": newPostForm(),

    })

@login_required
def post(request, id):
    posts = Post.objects.all().select_related('category')
    post = Post.objects.get(pk=id)
    isauthor = request.user.username == post.author.username
    recent_posts = Post.objects.all().order_by("-id")[:5]
    comments = Comment.objects.filter(post=post)
    recent_comments = Comment.objects.filter(post=post).order_by("-id")

    from django.core.paginator import Paginator

    p = Paginator(posts, 6)  # or whatever number suits your layout
    page_number = request.GET.get("page")
    page = p.get_page(page_number)

    return render(request, "mysite/post.html", {
        'posts': posts,
        'post': post,
        'page': page,
        'isauthor': isauthor,
        "comments": comments,
        'recent_posts': recent_posts,
        "recent_comments": recent_comments,
        "categories": Category.objects.all()
    })

@login_required
def dashboard(request):
    recent_posts = Post.objects.order_by('-date')[:5]
    recent_pages = Page.objects.all().order_by("-id")[:5]
    recent_comments = Comment.objects.order_by('-date')[:5]

    return render(request, 'mysite/dashboard.html', {'recent_posts': recent_posts, "recent_pages": recent_pages, 'recent_comments': recent_comments, })


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST':

        if request.user.id != post.author.id:
            return JsonResponse({"success": False, "error": "Unauthorized"})

        title = request.POST.get('title')
        body = request.POST.get('body')

        if not title or not body:
            return JsonResponse({"success": False, "error": "Missing fields"})

        post.title = title
        post.body = body
        post.save()

        messages.success(request, 'Post updated successfully!')
        return redirect('post', id=post.id)
    else:
        return render(request, 'mysite/edit_post.html', {'post': post})


def comment(request, id):
    user = request.user
    post_obj = Post.objects.get(pk=id)
    message = request.POST["new_comment"]

    new_comment = Comment(
        writor=user,
        post=post_obj,
        message=message
    )
    new_comment.save()

    return HttpResponseRedirect(reverse("post", args=[id]))


def addCategory(request, id):

    categoryName = request.POST['new_categoryName']
    category_obj, _ = Category.objects.get_or_create(categoryName=categoryName)

    post_obj = Post.objects.get(pk=id)
    post_obj.category = category_obj
    post_obj.save()

    return HttpResponseRedirect(reverse("post", args=[id]))

@login_required
def new_page(request, id):
    pages = Page.objects.all()
    page = Page.objects.get(pk=id)
    return render(request, "mysite/new_page.html", {
        'pages': pages,
        'page': page,
    })


def add_page(request):
    if request.method == "POST":
        form = newPageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)

            page.save()

            return redirect('new_page', id=page.id)
        else:
            return render(request, "mysite/add_page.html", {

                "form": form,  #  Preserve user input and show errors
                "message": "The form is invalid. Please resumbit"

            })
    else:
        return render(request, "mysite/add_page.html", {
            "form": newPageForm(),
            # "message": "page Created Successfully"

        })


def all_pages(request):
    pages = Page.objects.all().order_by("-id")
    recent_pages = Page.objects.all().order_by("-id")[:5]

    return render(request, "mysite/all_pages.html", {
        "pages": pages,
        "form": newPageForm(),
        "recent_pages": recent_pages,

    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "mysite/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "mysite/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mysite/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "mysite/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "mysite/register.html")
