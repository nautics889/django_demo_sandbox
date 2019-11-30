import datetime
from typing import Any

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from user_app.models import SandyUser


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: SandyUser,
                         timestamp: Any(str, datetime.datetime)):
        return (user.pk + timestamp + user.is_active)


account_activation_token = TokenGenerator()
