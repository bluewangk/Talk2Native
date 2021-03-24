# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogPageView(ListView):
    model = Post
    template_name = "blog.html"
      
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_create.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog_update.html'

class BlogDeleteView(DeleteView):
    model = Post
    # fields = '__all__'
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog')
    