from django.urls import path
from .views import BlogListView, PostDetailViiew, BlogCreateView

urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home' ),
    path('post/<int:pk>/', PostDetailViiew.as_view(), name='post_detail' ),
]