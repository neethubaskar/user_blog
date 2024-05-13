
from django.urls import path, include

from blog.v1.views import BlogPostListView


urlpatterns = [
    path('blog-list/', BlogPostListView.as_view(), name='blog_list'),
]