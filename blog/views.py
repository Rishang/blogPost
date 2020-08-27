from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# temp imports
import datetime
# from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "title": "My second blog",
        "desctiption": "Ok i quit",
        "author": "Rishang",
        "date": datetime.date.today,
    },
    {
        "title": "Man must explore, and this is exploration at its greatest",
        "desctiption": "I am thinking about what to write",
        "author": "Rishang",
        "date": datetime.date.today,
    }
]

aboutMe = ["Hello and welcome to My Blog WebPage","I am Current learning django"]


def home(request):
    
    return render(request,'blog/index.html',{"posts":posts})

def about(request):

    return render(request,'blog/about.html',{"about":aboutMe})

def post(request):

    return render(request,'blog/post.html')

def contact(request):
    
    return render(request,'blog/contact.html')