from celery import shared_task
from django.template.loader import get_template
from django.core import mail
from django.template.exceptions import TemplateDoesNotExist

from utils.logger import LOGGER


@shared_task
def send_mail_task(subject, message, sender, recipient_list,
                   template=None, context=None):
    """A task to send mails to recipient list.

    :param subject: (str) subject of a message
    :param message: (str) main message content
    :param sender: (str) email from
    :param recipient_list: (iterable) list of receivers
    :param template: (str) path to template
    :param context: (dict) context to be supplied to the template
    :return : (None)
    """
    try:
        content = get_template(template).render(context)
        messages_sent = mail.send_mail(subject, message, sender,
                                       recipient_list, html_message=content)
    except TemplateDoesNotExist as e:
        LOGGER.error('Provided template does not exist! %s', e)
        raise e
    except Exception as e:
        LOGGER.error('An error occurred during send mail:  %s', e)
        raise e
    else:
        LOGGER.debug('Successfully sent %s messages', messages_sent)
