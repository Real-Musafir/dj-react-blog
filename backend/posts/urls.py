from django.urls import path, re_path
from .views import PostListAPIView, CreatePost, PostDetail, PostUpdate, PostDelete
urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', CreatePost.as_view(), name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$',
            PostDetail.as_view(), name='detail'),
    path('edit/<str:slug>/', PostUpdate.as_view(), name='update'),
    re_path(r'^delete/(?P<slug>[\w-]+)/$',
            PostDelete.as_view(), name='delete'),
    # re_path(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    # path('<str:slug>/edit/', PostUpdateAPIView.as_view(), name='update'),
    # re_path(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),

]
