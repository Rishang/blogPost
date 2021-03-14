from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register_page'),
    path('login/',views.loginPage, name='login_page'),
    path('logout/',views.logoutUser, name='logout'),
    path('@<slug:slug>/', views.userListView.as_view(), name='user_profile'),
    path('<slug:slug>/edit', views.edit_profile, name='edit_profile'),
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_profile'),
]
