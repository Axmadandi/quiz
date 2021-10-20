from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path("", FirstView.as_view(), name="home"),
    path("register/", Register.as_view(), name="register"),
    path("ways/", ways, name="ways"),
    path("quiz/<slug>", quiz, name="main"),
]
