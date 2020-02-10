# God forgive me for star import
from .settings_base import *  # noqa


DEBUG = True

ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS += [
    'rest_framework',
    'drf_yasg',
    'oauth2_provider',
    'user_app.apps.UserAppConfig',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

AUTH_USER_MODEL = 'user_app.SandyUser'

OAUTH2_PROVIDER = {
    # list of available scopes
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope'
    }
}

CELERY_BROKER_URL = 'amqp://guest:guest@django_demo_sandbox_rabbitmq_1:5672/'

# Host for sending e-mail.
EMAIL_HOST = 'localhost' # for debugging purposes

# Port for sending e-mail.
EMAIL_PORT = 1025

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# Turn off security layers during development
EMAIL_USE_SSL = False
EMAIL_USE_TLS = False
