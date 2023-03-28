from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)

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


class UpdateBookView(UpdateView):
    model = models.Books
    template_name = "admin_panel/books/book_update.html"
    fields = "__all__"
    success_url = reverse_lazy("books_admin")


class DeleteBookView(DeleteView):
    template_name = "admin_panel/books/book_delete.html"
    success_url = reverse_lazy("books_admin")
    model = models.Books


class SearchBookView(View):
    def post(self, request):
        key_word = request.POST["search"]
        context = {
            "books": models.Books.objects.filter(title__contains=key_word),
            "search_word": key_word,
        }
        return render(request, "admin_panel/books/books_search.html", context=context)


# authors
class AuthorsListView(ListView):
    template_name = "admin_panel/authors/authors_list.html"
    model = models.Authors
    context_object_name = "authors"


class AddAuthorsView(CreateView):
    template_name = "admin_panel/authors/authors_create.html"
    form_class = forms.AuthorsForm
    success_url = "/admin_panel/authors/"


class UpdateAuthorView(UpdateView):
    model = models.Authors
    template_name = "admin_panel/authors/author_update.html"
    fields = "__all__"
    success_url = reverse_lazy("authors_admin")


class DeleteAuthorView(DeleteView):
    template_name = "admin_panel/authors/author_delete.html"
    success_url = reverse_lazy("authors_admin")
    model = models.Authors


class SearchBookView(View):
    def post(self, request):
        key_word = request.POST["search"]
        context = {
            "authors": models.Authors.objects.filter(name__contains=key_word),
            "search_word": key_word,
        }
        return render(
            request, "admin_panel/authors/authors_search.html", context=context
        )
