from django.urls import path
from .views import ( 
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    UserPostListView
)
from . import views 

urlpatterns = [
    path('', PostListView.as_view(), name= 'blog-home'), 
    path('user/<str:username>', UserPostListView.as_view(), name= 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post-detail'), #pk = primary key, the key for the post 
    path('post/<int:pk>/update', PostUpdateView.as_view(), name= 'post-update'), #update post
    path('about/', views.about, name= 'blog-about'),
    path('post/new/', PostCreateView.as_view(), name= 'post-create'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name= 'post-delete')
    
]