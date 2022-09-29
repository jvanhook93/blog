from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post



class PostListView(ListView):
  template_name = "posts/new.html"
  model = Post
  fields ["title", ]