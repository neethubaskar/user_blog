from django.db import models
from django.utils.text import slugify
from users.models import CustomUser

class BlogPost(models.Model):
    title = models.CharField(
        max_length=200, unique=True, help_text="Used to store the titleof the  blog.")
    slug = models.SlugField(max_length=200, unique=True, help_text="Blog unique slug.")
    author = models.ForeignKey(
        CustomUser, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField(help_text="Description about the blog.")
    created_on = models.DateTimeField(auto_now_add=True, help_text="Blog publishing date.")
    updated_on = models.DateTimeField(auto_now= True, help_text="Blog edited date.")
    is_active = models.BooleanField(
        default=True, db_index=True, help_text=(
            "Denotes the status of the blog. If false, denotes blog is currently unavailable."))

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
