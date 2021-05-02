from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ValidationError
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
import re
import random
import magic
import requests
from .unsplash import Unsplash

# Create your views here.

# class VIEWS

null_vals = ["", None]
class tagList(ListView):

    template_name = 'blog/tag.html'
    context_object_name = 'tag'
    
    def get_queryset(self):
        
        tag = self.kwargs['slug']
        tag_posts = Post.objects.filter(tags__name__in=[self.kwargs['slug']])
        related_tags = [tags.name for article in tag_posts for tags in article.tags.all()]
        return {
            'tag':tag,
            'tag_posts': tag_posts,
            'related_tags': related_tags
        }


"Validate POST request of form"
class ValidPost:
    def post(self, request, *args, **kwargs):
        
        form_tags = re.findall('\w+', request.POST.get('tags'))
        if len(form_tags) <= 15:
            for w in form_tags:
                if len(w) >= 15:
                    messages.info(request,f'Too long tag, {w}')
                    return redirect(request.path)
            return super().post(request, *args, **kwargs)
        else:
            messages.info(request,f'Max tags allowed 15, you gave {len(form_tags)}')
            return redirect(request.path)


class postList(ListView):
    
    # queryset = Post.objects.all()
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-datePosted']


class postDetail(DetailView):
    
    model = Post
    template_name = 'blog/post/post_form.html'
    template_name = 'blog/post/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs ['pk']

        post_instance = Post.objects.get(id=_id)
        context["user_post"] = Post.objects.filter(author=post_instance.author.id).exclude(pk=_id)
        return context


class postCreateView(LoginRequiredMixin, ValidPost, CreateView):

    model = Post
    fields = ['image','imageUrl','title','description','content','tags']
    login_url = reverse_lazy('login_page')
    template_name = 'blog/post/post_form.html'

    def form_valid(self, form):

        # set form author
        form.instance.author = self.request.user

        # do only if no image is uploaded in article post
        imageUrl = self.request.POST.get('imageUrl') or None
        image = self.request.POST.get('image') or None
        
        if imageUrl not in null_vals:
            url_data = requests.get(imageUrl)
            data_type = magic.from_buffer(url_data.content, mime=True)
            if data_type == 'image/jpeg':
                pass
            else:
                raise ValidationError("invalid image url")
        elif  image == None:

            d = Unsplash()

            # collect all tags
            form_tags = re.findall('\w+', self.request.POST['tags'])

            # search for images related to tags
            # and get random image instance
            q = d.query(search=form_tags, random_img=True)

            if len(q) != 0:
                # get image instance url, of regular size
                form.instance.imageUrl = q['urls']['regular']
            else:
                # get any random unsplash image url
                form.instance.imageUrl = d.any['urls']['regular']

        return super().form_valid(form) 


class postUpdateView(LoginRequiredMixin, UserPassesTestMixin, ValidPost, UpdateView):

    model = Post
    fields = ['image','imageUrl','title','description','content','tags']
    login_url = reverse_lazy('login_page')
    template_name = 'blog/post/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

         # do only if no image is uploaded in article post
        imageUrl = self.request.POST.get('imageUrl') or None
        
        if imageUrl not in null_vals:
            url_data = requests.get(imageUrl)
            data_type = magic.from_buffer(url_data.content, mime=True)
            if data_type == 'image/jpeg':
                pass
            else:
                messages.error(self.request, "invalid image url")
                return self.form_invalid(form)

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
    template_name = 'blog/post/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
             return False

# function based VIEW
def about(request):

    return render(request,'blog/about.html')
