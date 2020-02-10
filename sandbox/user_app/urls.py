from django.urls import re_path

from user_app.views import (SandyCurrentUserDetails,
                            SandyUserList,
                            activate_account)

urlpatterns = [
    re_path(
        '^$',
        SandyUserList.as_view(),
        name='list-create-users'
    ),
    re_path(
        '^my-profile$',
        SandyCurrentUserDetails.as_view(),
        name='retrieve-details-current-user'
    ),
    re_path(
        '^activate-account$',
        activate_account,
        name='activate-account'
    )
]
