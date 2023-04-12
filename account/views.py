from django.contrib.auth.models import User
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import RegisterForm


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("register")
    template_name = "account/register.html"


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "account/login.html"

    def get_success_url(self):
        return reverse_lazy("home")
