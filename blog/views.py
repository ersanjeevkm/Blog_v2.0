from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Posts
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.

class PostsList(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 7

class PostsDetail(DetailView):
    model = Posts
    template_name = 'blog/post.html'
    context_object_name = 'post'

class CreatePost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Posts
    template_name = 'blog/create_post.html'
    fields = ['title', 'content']
    success_message = "Post created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditPost(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Posts
    template_name = 'blog/edit_post.html'
    fields = ['title', 'content']
    success_message = 'Post edited successfully'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'blog/delete_post.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False

class UserPosts(ListView):
    model = Posts
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')
