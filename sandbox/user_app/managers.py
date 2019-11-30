from django.contrib.auth.models import BaseUserManager
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from user_app.mailer import Mailer
from user_app.token import account_activation_token


class SandyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self._create_user(username, email, password, **extra_fields)
        mailer = Mailer()
        mailer.send_messages(
            'subj',
            'confirm_registration_mail.html',
            {
                'username': user.username,
                'uid': urlsafe_base64_encode(
                    force_bytes(user.id)
                ),
                'token': account_activation_token.make_token(user)
            },
            [user.email, ]
        )
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
