from django.shortcuts import render
from .models import Post, PostView, Like, Comment, Category
from .serializers import CommentSerializer, PostSerializer, LikeSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


# Create your views here.

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status='p')
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.user.is_staff and self.action in ['destroy']:
            return super().get_permissions()
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class CommentView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class LikeView(APIView):
    pass