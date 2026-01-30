from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import CommentForm, PostForm, SearchForm
from .models import Comment, Post, Tag


# --- Home (hero + featured) ---
def home_view(request):
    featured = Post.objects.all()[:1].first()
    recent = Post.objects.all()[:3]
    return render(request, 'home.html', {
        'featured': featured,
        'recent_posts': recent,
    })


# --- Blog list with pagination ---
class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


# --- Post detail + comments ---
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context


# --- Add comment (POST) ---
class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if form.is_valid():
                Comment.objects.create(
                    post=post,
                    author=request.user,
                    body=form.cleaned_data['body'],
                )
                comments = post.comments.all()
                return JsonResponse({
                    'ok': True,
                    'html': render(request, 'partials/comment_list.html', {'comments': comments}).content.decode(),
                })
            return JsonResponse({'ok': False, 'error': 'Invalid comment'}, status=400)
        if form.is_valid():
            Comment.objects.create(
                post=post,
                author=request.user,
                body=form.cleaned_data['body'],
            )
        return redirect('post_detail', pk=pk)


# --- Create / Edit / Delete post ---
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    context_object_name = 'post'

    def test_func(self):
        return self.get_object().author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        return self.get_object().author == self.request.user


# --- Search ---
def search_view(request):
    form = SearchForm(request.GET or None)
    posts = []
    if form.is_valid() and form.cleaned_data.get('q'):
        q = form.cleaned_data['q'].strip()
        posts = Post.objects.filter(
            Q(title__icontains=q) | Q(body__icontains=q) | Q(excerpt__icontains=q)
        ).distinct()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    return render(request, 'search_results.html', {
        'form': form,
        'query': form.cleaned_data.get('q', '') if form.is_valid() else '',
        'posts': page_obj,
        'page_obj': page_obj,
    })


# --- About ---
def about_view(request):
    return render(request, 'about.html')


# --- Contact ---
def contact_view(request):
    return render(request, 'contact.html')


# --- User profile (user's posts) ---
def profile_view(request, username):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    return render(request, 'profile.html', {
        'profile_user': user,
        'posts': page_obj,
        'page_obj': page_obj,
    })
