from django.contrib import admin
from django.urls import path
from .views import index, TweetApiView

urlpatterns = [
    path('', index),
    path('tweets', TweetApiView.as_view())
]
