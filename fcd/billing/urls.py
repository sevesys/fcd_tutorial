from django.urls import path

from fcd.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "billing"
urlpatterns = [
    path("", view=billing_home, name="home"),
]
