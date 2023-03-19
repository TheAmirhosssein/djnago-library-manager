from django.shortcuts import render
from django.views.generic import DetailView, ListView

from library import models


class HomeView(ListView):
    template_name = "library/home.html"
    model = models.Books
    context_object_name = "books"


class BookDetailView(DetailView):
    template_name = "library/book_details.html"
    model = models.Books


class AuthorView(DetailView):
    template_name = "library/author.html"
    model = models.Authors


class TranslatorView(DetailView):
    template_name = "library/translators.html"
    model = models.Translators


class GenresView(DetailView):
    template_name = "library/genres.html"
    model = models.Genres
