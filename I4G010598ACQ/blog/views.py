from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post 
# Create your views here.

class PostListView(ListView):
      model = Post 
 
class PostCreateView(CreateView): 
      model = Post
      fields = "__all__"
      success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
       model = Post

class PostUdateView(UpdateView):
      model = Post
      fields = "__all__"
      success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
      model = Post
      fields = "__all__"
      success_url = reverse_lazy("blog:all")


