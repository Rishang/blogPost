from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about/', views.about, name="about_us"),
    path('post/', views.post, name='blog_post'),
    path('contact/', views.contact, name='contact_us'),
]