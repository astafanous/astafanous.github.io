from django.urls import path
from . import views

app_name = 'encyclopedia'

urlpatterns = [
     path("", views.index, name="index"),
     path("wiki/<str:title>", views.entry, name="entry"),
     path("modify/<str:title>", views.modify, name="modify"),
     path("search", views.search, name="search"),
     path("topics/", views.topics, name='topics'),
     path("randoms", views.randoms, name="randoms"),
    
     
     
     
 ]