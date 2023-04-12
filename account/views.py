from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, View

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


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("login"))
