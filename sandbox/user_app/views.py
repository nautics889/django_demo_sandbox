from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import generics, permissions

from user_app.models import SandyUser
from user_app.serializers import SandyUserSerializer
from user_app.mailer import Mailer

# TODO: update view for signup, create token confirm view


class SandyUserList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = SandyUser.objects.all()
    serializer_class = SandyUserSerializer

    def get(self, request, *args, **kwargs):
        mailer = Mailer()
        mailer.send_messages(
            'subject',
            'confirm_registration_mail.html',
            {'debug_msg': 'qwerty123'},
            ['cyberukr@gmail.com', ]
        )
        return super(SandyUserList, self).get(request, *args, **kwargs)


class SandyCurrentUserDetails(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)
    serializer_class = SandyUserSerializer

    def get_object(self):
        return self.request.user
