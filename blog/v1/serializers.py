from rest_framework import serializers
from blog.models import BlogPost


class BlogPostListSerializer(serializers.ModelSerializer):
    published_date = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'author', 'content', 'published_date')

    def get_published_date(self, obj):
        return obj.created_on.strftime('%Y-%m-%d %H:%M:%S')

    def get_author(self, obj):
        return obj.author.first_name + ' ' + obj.author.last_name


class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializer for the BlogPost model.
    """
    class Meta:
        model = BlogPost
        fields = '__all__'
        # Exclude slug and author fields from validation
        read_only_fields = ('slug', 'author')

    