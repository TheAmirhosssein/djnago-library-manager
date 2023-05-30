from django.db.models import Count
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from components.wikipedia_api import get_wikipedia_page
from library import models


class HomeView(ListView):
    template_name = "library/home.html"
    model = models.Books
    context_object_name = "books"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context["authors"] = models.Authors.objects.annotate(books_count=Count('books')).all()
        return context
    
    def get_queryset(self):
        query = super(HomeView, self).get_queryset()
        q = self.request.GET.get("q")
        author = self.kwargs.get("author")
        if q is not None:
            query = query.filter(title__contains=q)
        if author is not None:
            query = query.filter(author__slug=author)
        return query
    


class BookDetailView(DetailView):
    template_name = "library/book_details.html"
    model = models.Books
    context_object_name = "book"


class AuthorView(DetailView):
    template_name = "library/author.html"
    model = models.Authors
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        context = super(AuthorView, self).get_context_data(**kwargs)
        author_slug = self.kwargs.get("slug")
        author = models.Authors.objects.get(slug=author_slug)
        context["author_info"] = get_wikipedia_page(author.name)
        context["books"] = models.Books.objects.filter(author__slug=author_slug)
        return context


class TranslatorView(DetailView):
    template_name = "library/translators.html"
    model = models.Translators


class GenresView(DetailView):
    template_name = "library/genres.html"
    model = models.Genres
