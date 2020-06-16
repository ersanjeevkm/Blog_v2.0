from django.urls import path
from .views import PostsList, PostsDetail, CreatePost, EditPost, DeletePost, UserPosts

urlpatterns = [
    path('', PostsList.as_view(), name='home'),
    path('post/<int:pk>', PostsDetail.as_view(), name='post'),
    path('post/create', CreatePost.as_view(), name='create_post'),
    path('post/edit/<int:pk>', EditPost.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
    path('post/<str:username>', UserPosts.as_view(), name='user_posts')
]
