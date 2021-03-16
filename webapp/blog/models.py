from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=300)
    content = models.TextField(blank=True)
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='post_images')
    tags = TaggableManager()

    def __str__(self):
        return f'{self.title} | {self.author} | {self.datePosted}'
    def get_absolute_url(self):
        return reverse('blog_home')
