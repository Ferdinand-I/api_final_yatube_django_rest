from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PostModelViewSet, GroupViewSet, CommentViewSet, FollowViewSet
)


router = DefaultRouter()
router.register(r'posts', PostModelViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'^posts/(?P<post_pk>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
