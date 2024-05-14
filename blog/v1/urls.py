
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.v1.views import BlogPostListView, BlogPostViewSet

router = DefaultRouter()
router.register(r'blogposts', BlogPostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('blog-list/', BlogPostListView.as_view(), name='blog_list'),
]