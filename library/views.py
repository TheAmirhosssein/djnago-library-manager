from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = "library/home.html"


class BookDetailView(TemplateView):
    template_name = "library/book_details.html"
