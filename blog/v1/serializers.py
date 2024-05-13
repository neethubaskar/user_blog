from rest_framework import serializers
from blog.models import BlogPost


class BlogPostListSerializer(serializers.ModelSerializer):
    published_date = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'author', 'content', 'published_date')

    def get_published_date(self, obj):
        return obj.created_on
    