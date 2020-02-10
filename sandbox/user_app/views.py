from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from user_app.token import account_activation_token

from user_app.models import SandyUser
from user_app.serializers import SandyUserSerializer

# TODO: update view for signup, create token confirm view


class SandyUserList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = SandyUser.objects.all()
    serializer_class = SandyUserSerializer


class SandyCurrentUserDetails(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)
    serializer_class = SandyUserSerializer

    def get_object(self):
        return self.request.user


@api_view(['GET', ])
def activate_account(request):
    encoded_uid = request.query_params.get('euid', '')
    token = request.query_params.get('token', '')
    try:
        uid = force_text(urlsafe_base64_decode(encoded_uid))
        user = SandyUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, SandyUser.DoesNotExist) as e:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response(status=200)
    return Response(data={'error': 'Invalid token'}, status=400)

