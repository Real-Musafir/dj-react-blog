from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    BasePermission
)
from .serializers import (
    PostListSerializer,
    PostCreateSerializer,
    PostDetailSerializer,
    PostCreateSerializer
)
from posts.models import Post

from rest_framework.parsers import MultiPartParser, FormParser
from .permissions import IsOwnerOrReadOnly


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Post.objects.all()
        return queryset_list


class CreatePost(APIView):
    permission_classes = [IsAuthenticated]
    # this because we want to upload image
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data, "From Create Data")
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostUpdate(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)


class PostDelete(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [BasePermission]


# class PostDelete(RetrieveDestroyAPIView):
#     permission_classes = [IsOwnerOrReadOnly]
#     serializer_class = PostDetailSerializer
#     queryset = Post.objects.all()
#     lookup_field = 'slug'
