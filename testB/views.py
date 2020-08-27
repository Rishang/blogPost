from django.shortcuts import render
from .models import Post


# Create your views here.

def home(request):
    posts = {}
    for post in Post.objects.all():
        context = {
            'title': post.title,
            'description': post.description,
            'postId': post.id
        }
        post[f"{post.id}"] = context
    return render(request, '')

def post(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'testB/post.html', context)
