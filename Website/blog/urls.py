from django.conf.urls import url, include
from django.urls import re_path
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [
    re_path('(?P<pk>(\d+))', DetailView.as_view(model=Post, template_name="blog/post.html")),
    url('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                template_name="blog/blog.html"))

]
