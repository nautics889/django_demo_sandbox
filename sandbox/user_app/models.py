from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin,
                                        UserManager)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.text import gettext_lazy as _


class SandyUser(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(
        _('username'),
        max_length=20,
        unique=True,
        help_text=_(
            'Required. 20 characters or fewer. '
            'Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'))
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    status = models.CharField(
        _('status'),
        default="Some cool status",
        max_length=120
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']


class BlackListUnit(models.Model):
    blocker = models.ForeignKey(
        SandyUser,
        on_delete=models.CASCADE,
        related_name='blocker_user'
    )
    blocked = models.ForeignKey(
        SandyUser,
        on_delete=models.CASCADE,
        related_name='blocked_users'
    )
    timestamp = models.DateTimeField()

    def save(self, *args, **kwargs) -> None:
        if self.blocked.id == self.blocker.id:
            raise ValueError('User can not add himself to blacklist.')
        super(BlackListUnit, self).save(*args, **kwargs)
