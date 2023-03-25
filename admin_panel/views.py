from django.shortcuts import render
from django.views.generic import CreateView, FormView, ListView, TemplateView

from admin_panel import forms
from library import models


class DashboardView(TemplateView):
    template_name = "admin_panel/admin_panel.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data()
        context["books"] = models.Books.objects.all()
        context["authors"] = models.Authors.objects.all()
        context["publishers"] = models.Publishers.objects.all()
        context["translators"] = models.Translators.objects.all()
        return context


# books view
class BooksListView(ListView):
    template_name = "admin_panel/books/books_list.html"
    model = models.Books
    context_object_name = "books"


class AddBookView(CreateView):
    template_name = "admin_panel/books/books_create.html"
    form_class = forms.BooksForm
    success_url = "/admin_panel/books/"
