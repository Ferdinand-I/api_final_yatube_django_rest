from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .permissions import AuthorOrReadOnly
from .serializers import (
    PostSerializer, GroupSerailizer,
    CommentSerializer, FollowSerializer
)
from posts.models import Post, Group, Follow


class PostModelViewSet(ModelViewSet):
    """ViewSet class that provides api view based on Post model."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """ViewSet class that provides api view based on Group model."""
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Group.objects.all()
    serializer_class = GroupSerailizer


class CommentViewSet(ModelViewSet):
    """ViewSet class that provides api view based on Comment model."""
    permission_classes = (AuthorOrReadOnly, )
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Method that helps to get specific queryset
        that depends on request params.
        """
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer) -> None:
        """Overrided method to create new specific serialized data."""
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(
            author=self.request.user,
            post=post
        )


class FollowViewSet(ModelViewSet):
    """ViewSet class that provides api view based on Follow model."""
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        """Method that helps to get specific queryset
        that depends on request params.
        """
        user = self.request.user
        queryset = Follow.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(
            user=user
        )
