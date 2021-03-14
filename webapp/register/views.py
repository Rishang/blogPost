from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .register import (
    CreateUser, UserCreationForm, User,
    UserUpdateForm, ProfileUpdateForm
)
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, DeleteView
from blog.models import Post
from .models import Profile

# Create your views here.

"Display profile data of user"
class userListView(ListView):

    template_name = 'profile/index.html'
    context_object_name = 'slugUser'
    ordering = ['-datePosted']

    def get_queryset(self):

        user_page = User.objects.get(username=self.kwargs ['slug'])
        user_post = Post.objects.filter(author=user_page.id)
        user_post_count = user_post.count()
        user_profile = Profile.objects.get(user=user_page)

        return {
            "post": user_post,
            "total_post": user_post_count,
            "profile": user_profile
        }

"Delete user account"
class DeleteUser(DeleteView):

    model = User
    template_name = 'profile/delete.html'
    login_url = reverse_lazy('login_page')
    success_url = reverse_lazy('blog_home')

"register user"
def register(request):

    regForm = CreateUser(request.POST or None)
    if regForm.is_valid():
        regForm.save()
        username = regForm.cleaned_data.get('username')
        messages.success(request, f'Account created for {username} !!')

        return redirect('login_page')
        
    return render(request,'register/index.html', {"register":regForm})
"login as user"
def loginPage(request):
    
    if request.method == 'POST':
        
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        isUser = authenticate(request, username=username ,password=password)
        # isUser = authenticate(request, email=email ,password=password)

        if isUser is not None:
            
            if isUser.is_staff:
                messages.info(request, 'Staff users can\'t login from here')
                return redirect('login_page')
            login(request, isUser)
            messages.success(request, f'{isUser} Logged in !')
            
            return redirect('blog_home')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login_page')

    return render(request,'login/login.html')

"logout"
@login_required(redirect_field_name='login',login_url='login_page')
def logoutUser(request):
    logout(request)
    return redirect('login_page')


"Edit user profile"
@login_required(redirect_field_name='login',login_url='login_page')
def edit_profile(request,**kwargs):

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f"Account updated!")

            return redirect('user_profile', request.user.username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request,'profile/updateForm.html', context)
