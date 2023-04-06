from django.shortcuts import render
from django.views.generic import DetailView, ListView

from components.wikipedia_api import get_wikipedia_page
from library import models


class HomeView(ListView):
    template_name = "library/home.html"
    model = models.Books
    context_object_name = "books"


class BookDetailView(DetailView):
    template_name = "library/book_details.html"
    model = models.Books
    context_object_name = "book"


class AuthorView(DetailView):
    template_name = "library/author.html"
    model = models.Authors

    def get_context_data(self, **kwargs):
        context = super(AuthorView, self).get_context_data(**kwargs)
        author = models.Authors.objects.get(slug=self.kwargs.get("slug"))
        context["author_info"] = get_wikipedia_page(author.name)
        return context


class TranslatorView(DetailView):
    template_name = "library/translators.html"
    model = models.Translators


class GenresView(DetailView):
    template_name = "library/genres.html"
    model = models.Genres
