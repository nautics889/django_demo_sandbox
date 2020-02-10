from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from user_app.models import SandyUser
from user_app.tasks import send_mail_task
from user_app.token import account_activation_token
from utils import LOGGER


@receiver(post_save, sender=SandyUser)
def send_confirm_registration_token(sender, instance, created, **kwargs):
    if not created:
        return None

    LOGGER.info('POST SAVE SIGNAL')

    send_mail_task.delay(
        subject='Confirmation mail',
        message='Confirm your registration',
        sender='sandbox@sand.box',
        recipient_list=[instance.email, ],
        template='confirm_registration_mail.html',
        context={
            'username': instance.username,
            'uid': urlsafe_base64_encode(
                force_bytes(instance.id)
            ),
            'token': account_activation_token.make_token(instance)
        }
    )
