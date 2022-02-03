from rest_framework.viewsets import ModelViewSet

from post.api.serializers import PostSerializer
from post.models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer