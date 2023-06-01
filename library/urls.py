from django.urls import path

from library.views import (AuthorView, BookDetailView, GenresView, HomeView,
                           TranslatorView)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("books_filter/<author>/", HomeView.as_view(), name="author_filter"),
    path("book/<slug>/", BookDetailView.as_view(), name="book_details"),
    path("author/<slug>/", AuthorView.as_view(), name="author"),
    path("translator/<slug>/", TranslatorView.as_view(), name="translator"),
    path("genres/<slug>/", GenresView.as_view(), name="genres"),
]
