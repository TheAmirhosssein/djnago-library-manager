from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import RegisterForm


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("register")
    template_name = "account/register.html"



# class CreateUser(SetNotAccessMixin, ReturnIfAuthenticateMixin, CreateView):
#     form_class = UserForm
#     model = User

#     def form_valid(self, form):
#         user = form.save(commit=False)
#         user.is_active = False
#         user.save()
#         return render(self.request, "email-confirmation/email_send_login.html")

#     # if is success rever user to login page
#     success_url = reverse_lazy("login")
#     # our template name
#     template_name = "registration/signup.html"
