from django.shortcuts import render
from django.views.generic import CreateView

from account.forms import RegisterForm


class RegisterView(CreateView):
    template_name = "account/register.html"
    form_class = RegisterForm
    success_url = "/account/register/"
