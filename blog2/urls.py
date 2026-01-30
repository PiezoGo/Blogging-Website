from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.BlogListView.as_view(), name='post_list'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.BlogEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('search/', views.search_view, name='search'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
]
