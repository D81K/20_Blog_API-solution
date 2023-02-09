from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PostViewSet)


urlpatterns = [
    path('comment/', CommentView.as_view()),
    path('like/<str:slug>/', LikeView.as_view()),
] + router.urls