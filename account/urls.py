from django.urls import path

from account import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
]
