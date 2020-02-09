from unittest.mock import patch

from django.test import TestCase
from django.template.exceptions import TemplateDoesNotExist

from user_app.tasks import send_mail_task


class SendMailTaskTest(TestCase):
    @patch('django.core.mail.send_mail')
    def test_valid_data(self, send_mail):
        send_mail_task('subj',
                       'Message',
                       'from@e.mail',
                       ['to@e.mail', ],
                       template='confirm_registration_mail.html',
                       context=dict())
        send_mail.assert_called_once()

    def test_non_existing_template(self):
        with self.assertRaises(TemplateDoesNotExist):
            send_mail_task('subj',
                           'Message',
                           'from@e.mail',
                           ['to@e.mail', ],
                           template='non_existing_template',
                           context=dict())
