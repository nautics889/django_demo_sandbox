from rest_framework import generics, permissions
from user_app.models import SandyUser
from user_app.serializers import SandyUserSerializer


class SandyUserList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = SandyUser.objects.all()
    serializer_class = SandyUserSerializer


class SandyUserDetails(generics.RetrieveAPIView):
    pass
