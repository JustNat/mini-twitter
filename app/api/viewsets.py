from rest_framework import viewsets
from app.api import serializer 
from app import models

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserSerializer
    queryset = models.User.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.PostSerializer
    queryset = models.Post.objects.all()

