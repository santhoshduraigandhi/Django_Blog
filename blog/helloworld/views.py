from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import APIView

from .serializers import PostSerializers
from rest_framework.viewsets import ModelViewSet
from .models import Post

from rest_framework.permissions import IsAuthenticated
from .permissions import IsPostOwner
from rest_framework import filters

from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class HelloWorlView(APIView):
    def get(self,request):
        return Response({"info":"Hello World"})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated,IsPostOwner]
    # queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filter_class = PostFilter
    search_fields = ['title', 'content']

    def get_queryset(self):
        return Post.objects.filter(created_by = self.request.user)