from django.urls import path

from library.views import HomeView

urlpatterns = [path("", HomeView.as_view(), name="home")]
