from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #can't use decorator on class, use mixin instead. 
#basically sth that the class inherits from 
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ( 
    ListView, 
    DetailView,
    CreateView,
    UpdateView, 
    DeleteView 
)
from .models import Post

#a list of dictionaries containing information of each post
# Create your views here.

#Handle the traffic from the homepage in the blog
"""
def home(request): 
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) # pass the posts data into the template and let us access from the templates
"""
class PostListView(ListView): 
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView): 
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self): 
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView): 
    model = Post #if named according to convention, only needs one line

class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user #set the author to the current logged in user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user #set the author to the current logged in user
        return super().form_valid(form)
    
    def test_func(self): 
        post = self.get_object() #get the post we're trying to update
        if self.request.user == post.author: 
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Post #if named according to convention, only needs one line
    success_url = "/"
    def test_func(self): 
        post = self.get_object() #get the post we're trying to update
        if self.request.user == post.author: 
            return True
        return False
def about(request): 
    return render(request, 'blog/about.html', {'title': 'About Catto Blog'})

#different kinds of class-based views: list views, details views, create, update views 

