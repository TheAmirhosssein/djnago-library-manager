from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from library import models


class HomeView(TemplateView):
    template_name = "library/home.html"


class BookDetailView(DetailView):
    template_name = "library/book_details.html"
    model = models.Books


class AuthorView(DetailView):
    template_name = "library/author.html"
    model = models.Authors
