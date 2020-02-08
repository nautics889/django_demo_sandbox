from celery import shared_task
from django.template.loader import get_template
from django.core import mail


@shared_task
def send_mail_task(subject, message, sender, recipient_list,
                   template=None, context=None):
    """A task to send mails to recipient list.

    :param subject (str): subject of a message
    :param message (str): main message content
    :param sender (str): email from
    :param recipient_list (iterable): list of receivers
    :param template (str): path to template
    :param context (dict): context to be supplied to the template
    :return (None):
    """
    content = get_template(template).render(context)
    mail.send_mail(subject, message, sender,
                   recipient_list, html_message=content)

