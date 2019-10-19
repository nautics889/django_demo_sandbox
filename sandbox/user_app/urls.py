from django.urls import re_path
from user_app.views import SandyUserList

urlpatterns = [
    re_path(
        '^$',
        SandyUserList.as_view(),
        name='list-create-users'
    ),
]
