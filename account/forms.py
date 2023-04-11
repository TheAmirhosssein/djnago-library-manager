from django import forms
from django.contrib.auth.forms import (PasswordChangeForm, SetPasswordForm,
                                       UserCreationForm)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# registration user form
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=60, required=True, help_text="Fast Name")
    last_name = forms.CharField(max_length=60, required=True, help_text="Last Name")
    username = forms.CharField(max_length=150, required=True, help_text="Username")
    email = forms.EmailField(max_length=254, required=True, help_text="Email")

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

