from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import generics, permissions

from user_app.models import SandyUser
from user_app.serializers import SandyUserSerializer


class SandyUserList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = SandyUser.objects.all()
    serializer_class = SandyUserSerializer

class SandyCurrentUserDetails(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)
    serializer_class = SandyUserSerializer

    def get_object(self):
        return self.request.user
