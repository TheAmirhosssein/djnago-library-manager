from django.urls import path

from library.views import BookDetailView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("book/<slug>/", BookDetailView.as_view(), name="details"),
]
