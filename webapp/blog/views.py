from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# CRUD
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from register.models import Profile

# reverse urls
from django.urls import reverse_lazy

# models
from .models import Post,User

# from django.http import HttpResponse


# Create your views here.

# class VIEWS

class postList(ListView):
    
    # queryset = Post.objects.all()
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-datePosted']

class postDetail(DetailView):
    
    model = Post
    template_name = 'blog/post_form.html'
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs ['pk']

        post_instance = Post.objects.get(id=_id)
        context["user_post"] = Post.objects.filter(author=post_instance.author.id).exclude(pk=_id)
        return context

class postCreateView(LoginRequiredMixin,CreateView):

    model = Post
    fields = ['image','title','description','content']
    login_url = reverse_lazy('login_page')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class postUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['image','title','description','content']
    login_url = reverse_lazy('login_page')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
             return False

class postDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Post
    login_url = reverse_lazy('login_page')
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
             return False

# function based VIEW
def about(request):

    return render(request,'blog/about.html')
