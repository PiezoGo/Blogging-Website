from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView,UpdateView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailViiew(DeleteView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']