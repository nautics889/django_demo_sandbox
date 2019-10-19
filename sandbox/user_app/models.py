from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class SandyUser(AbstractUser):
    status = models.CharField(max_length=120)


class BlackListUnit(models.Model):
    blocker = models.ForeignKey(SandyUser,
                                on_delete=models.CASCADE,
                                related_name='blocker_user')
    blocked = models.ForeignKey(SandyUser,
                                on_delete=models.CASCADE,
                                related_name='blocked_users')
    timestamp = models.DateTimeField()

    def save(self, *args, **kwargs) -> None:
        if self.blocked.id == self.blocker.id:
            raise ValueError('User can not add himself to blacklist.')
        super(BlackListUnit, self).save(*args, **kwargs)
