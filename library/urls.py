from django.urls import path

from library.views import AuthorView, BookDetailView, HomeView, TranslatorView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("book/<slug>/", BookDetailView.as_view(), name="book_details"),
    path("author/<slug>/", AuthorView.as_view(), name="author"),
    path("translator/<slug>/", TranslatorView.as_view(), name="translator"),
]
