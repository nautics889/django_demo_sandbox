from django.urls import re_path

from user_app.views import SandyCurrentUserDetails, SandyUserList

urlpatterns = [
    re_path(
        '^$',
        SandyUserList.as_view(),
        name='list-create-users'
    ),
    re_path(
        '^my_profile$',
        SandyCurrentUserDetails.as_view(),
        name='retrieve-details-current-user'
    ),
]
