from django import forms
from django.contrib.auth.forms import (
    PasswordChangeForm,
    SetPasswordForm,
    UserCreationForm,
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# registration user form
class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=60, required=True, help_text="Fast Name")
    last_name = forms.CharField(max_length=60, required=True, help_text="Last Name")
    username = forms.CharField(max_length=150, required=True, help_text="Username")
    email = forms.EmailField(max_length=254, required=True, help_text="Email")
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("password2")
        if password == confirm_password:
            return confirm_password

        raise ValidationError("کلمه عبور و تکرار کلمه عبور مغایرت دارند")
