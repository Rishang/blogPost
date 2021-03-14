from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

"User profile class"
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to = "profile_images",
        null = True,
        blank = True
    )
    about = models.TextField(blank=True, null=True, max_length=2000)
    social_insta = models.URLField(blank=True, null=True)
    social_facebook = models.URLField(blank=True, null=True)
    social_twitter = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} Profile"

    def get_absolute_url(self):
        return reverse('user_profile')
