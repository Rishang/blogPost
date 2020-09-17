from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList.as_view(), name='blog_home'),
    path('post/<int:pk>/', views.postDetail.as_view(), name='blog_post'),
    path('post/new/',views.postCreateView.as_view(), name='blog_new'),
    path('post/<int:pk>/edit/', views.postUpdateView.as_view(), name='blog_edit'),
    path('post/<int:pk>/delete/', views.postDeleteView.as_view(), name='blog_delete'),
    path('about/', views.about, name="about_us"),
]