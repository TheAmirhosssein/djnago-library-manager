from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from library import models

# Create your views here.


class HomeView(TemplateView):
    template_name = "library/home.html"


class BookDetailView(TemplateView):
    template_name = "library/book_details.html"
    model = models.Books
