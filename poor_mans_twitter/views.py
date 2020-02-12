from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Tweet
from .serializers import TweetSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

def index(request):
    return render(request, 'index.html', context={
        'is_authenticated': request.user.is_active
    })


class TweetApiView(ListCreateAPIView):
    queryset = Tweet.objects.all().order_by('-date', 'name')
    serializer_class = TweetSerializer
    permission_classes = [AllowAny]