from django.urls import path
from .views import BlogListView, PostDetailViiew, BlogCreateView, BlogEditView, BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlogEditView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home' ),
    path('post/<int:pk>/', PostDetailViiew.as_view(), name='post_detail' ),
]