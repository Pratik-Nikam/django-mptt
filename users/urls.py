from django.conf.urls import url,include
from users.views import dashboard
from users.views import dashboard, register

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^$", dashboard, name="dashboard"),
   
    url(r"^register/", register, name="register"),
]

