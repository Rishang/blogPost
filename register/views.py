from django.shortcuts import render, redirect

from .register import CreateUser, UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        regForm = CreateUser(request.POST)
        if regForm.is_valid():
            regForm.save()
            username = regForm.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !!')

            return redirect('login_page')
        
    else:        
        regForm = CreateUser()
            
    return render(request,'register/index.html', {"register":regForm})

def loginPage(request):
    
    if request.method == 'POST':
        
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        isUser = authenticate(request, username=username ,password=password)
        # isUser = authenticate(request, email=email ,password=password)

        if isUser is not None:
            login(request, isUser)
            messages.success(request, f'{isUser} Logged in !')
            return redirect('blog_home')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login_page')

    return render(request,'login/login.html')

@login_required(redirect_field_name='login',login_url='login_page')
def logoutUser(request):
    logout(request)
    return redirect('login_page')