from rest_framework.viewsets import ModelViewSet

from user.api.serializers import UserSerializer
from user.models import User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer