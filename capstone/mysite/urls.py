from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("create", views.create_post, name="create"),
    path("post/<int:id>", views.post, name="post"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("all_posts", views.all_posts, name="all_posts"),
    path("edit_post/<int:id>", views.edit_post, name="edit_post"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("addCategory/<int:id>", views.addCategory, name="addCategory"),
    path("page_home", views.page_home, name="page_home"),
    path("new_page/<int:id>", views.new_page, name="new_page"),
    path("add_page", views.add_page, name="add_page"),
    path("all_pages", views.all_pages, name="all_pages"),

]
