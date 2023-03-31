from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
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


class DashboardView(PermissionRequiredMixin, TemplateView):
    permission_required = "library.action_all"
    template_name = "admin_panel/admin_panel.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data()
        context["books"] = models.Books.objects.all()
        context["authors"] = models.Authors.objects.all()
        context["publishers"] = models.Publishers.objects.all()
        context["translators"] = models.Translators.objects.all()
        return context


# books view
class BooksListView(PermissionRequiredMixin, ListView):
    permission_required = "library.action_all"
    template_name = "admin_panel/books/books_list.html"
    model = models.Books
    context_object_name = "books"


class AddBookView(PermissionRequiredMixin, CreateView):
    permission_required = "library.action_all"
    template_name = "admin_panel/books/books_create.html"
    form_class = forms.BooksForm
    success_url = "/admin_panel/books/"


class UpdateBookView(PermissionRequiredMixin, UpdateView):
    permission_required = "library.action_all"
    model = models.Books
    template_name = "admin_panel/books/book_update.html"
    fields = "__all__"
    success_url = reverse_lazy("books_admin")


class DeleteBookView(PermissionRequiredMixin, DeleteView):
    permission_required = "library.action_all"
    template_name = "admin_panel/books/book_delete.html"
    success_url = reverse_lazy("books_admin")
    model = models.Books


class SearchBookView(PermissionRequiredMixin, View):
    permission_required = "library.action_all"

    def post(self, request):
        key_word = request.POST["search"]
        context = {
            "books": models.Books.objects.filter(title__contains=key_word),
            "search_word": key_word,
        }
        return render(request, "admin_panel/books/books_search.html", context=context)


# authors
class AuthorsListView(PermissionRequiredMixin, ListView):
    permission_required = "library.action_all"
    template_name = "admin_panel/authors/authors_list.html"
    model = models.Authors
    context_object_name = "authors"


class AddAuthorsView(PermissionRequiredMixin, CreateView):
    permission_required = "library.action_all"
    template_name = "admin_panel/authors/authors_create.html"
    form_class = forms.AuthorsForm
    success_url = "/admin_panel/authors/"


class UpdateAuthorView(PermissionRequiredMixin, UpdateView):
    permission_required = "library.action_all"
    model = models.Authors
    template_name = "admin_panel/authors/author_update.html"
    fields = "__all__"
    success_url = reverse_lazy("authors_admin")


class DeleteAuthorView(PermissionRequiredMixin, DeleteView):
    permission_required = "library.action_all"
    template_name = "admin_panel/authors/author_delete.html"
    success_url = reverse_lazy("authors_admin")
    model = models.Authors


class SearchAuthorView(PermissionRequiredMixin, View):
    permission_required = "library.action_all"

    def post(self, request):
        key_word = request.POST["search"]
        context = {
            "authors": models.Authors.objects.filter(name__contains=key_word),
            "search_word": key_word,
        }
        return render(
            request, "admin_panel/authors/authors_search.html", context=context
        )


# publishers
class PublishersListView(PermissionRequiredMixin, ListView):
    permission_required = "library.action_all"
    template_name = "admin_panel/publishers/publishers_list.html"
    model = models.Publishers
    context_object_name = "publishers"


class AddPublishersView(PermissionRequiredMixin, CreateView):
    permission_required = "library.action_all"
    template_name = "admin_panel/publishers/publishers_create.html"
    form_class = forms.PublishersForm
    success_url = "/admin_panel/publishers/"


class UpdatePublisherView(PermissionRequiredMixin, UpdateView):
    permission_required = "library.action_all"
    model = models.Publishers
    template_name = "admin_panel/publishers/publisher_update.html"
    fields = "__all__"
    success_url = reverse_lazy("publishers_admin")


class DeletePublisherView(PermissionRequiredMixin, DeleteView):
    permission_required = "library.action_all"
    template_name = "admin_panel/publishers/publisher_delete.html"
    success_url = reverse_lazy("publishers_admin")
    model = models.Publishers


class SearchPublishersView(PermissionRequiredMixin, View):
    permission_required = "library.action_all"

    def post(self, request):
        key_word = request.POST["search"]
        context = {
            "publishers": models.Publishers.objects.filter(title__contains=key_word),
            "search_word": key_word,
        }
        return render(
            request, "admin_panel/publishers/publishers_search.html", context=context
        )


# translators
class TranslatorListView(PermissionRequiredMixin, ListView):
    permission_required = "library.action_all"
    template_name = "admin_panel/translators/translators_list.html"
    model = models.Translators
    context_object_name = "translators"


class AddTranslatorView(PermissionRequiredMixin, CreateView):
    permission_required = "library.action_all"
    template_name = "admin_panel/translators/translators_create.html"
    form_class = forms.TranslatorsForm
    success_url = "/admin_panel/translators/"


class UpdateTranslatorView(PermissionRequiredMixin, UpdateView):
    permission_required = "library.action_all"
    model = models.Translators
    template_name = "admin_panel/translators/translator_update.html"
    fields = "__all__"
    success_url = reverse_lazy("translators_admin")


class DeleteTranslatorView(PermissionRequiredMixin, DeleteView):
    permission_required = "library.action_all"
    model = models.Translators
    template_name = "admin_panel/translators/translator_delete.html"
    success_url = reverse_lazy("translators_admin")


class SearchTranslatorsView(PermissionRequiredMixin, View):
    permission_required = "library.action_all"

    def post(self, request):
        key_word = request.POST["search"]
        context = {
            "translators": models.Translators.objects.filter(name__contains=key_word),
            "search_word": key_word,
        }
        return render(
            request, "admin_panel/translators/translators_search.html", context=context
        )


# genres
class GenresListView(PermissionRequiredMixin, ListView):
    permission_required = "library.action_all"
    model = models.Genres
    template_name = "admin_panel/genres/genres_list.html"
    context_object_name = "genres"


class AddGenresView(PermissionRequiredMixin, CreateView):
    permission_required = "library.action_all"
    form_class = forms.GenresForm
    template_name = "admin_panel/genres/genres_create.html"
    success_url = "/admin_panel/genres/"


class UpdateGenresView(PermissionRequiredMixin, UpdateView):
    permission_required = "library.action_all"
    model = models.Genres
    template_name = "admin_panel/genres/genres_update.html"
    fields = "__all__"
    success_url = reverse_lazy("genres_admin")


class DeleteGenreView(PermissionRequiredMixin, DeleteView):
    permission_required = "library.action_all"
    model = models.Genres
    template_name = "admin_panel/genres/genres_delete.html"
    success_url = reverse_lazy("genres_admin")


class SearchGenresView(PermissionRequiredMixin, View):
    permission_required = "library.action_all"

    def post(self, request):
        key_word = request.POST["search"]
        context = {
            "genres": models.Genres.objects.filter(title__contains=key_word),
            "search_word": key_word,
        }
        return render(request, "admin_panel/genres/genres_search.html", context=context)


# users
class UsersListView(PermissionRequiredMixin, ListView):
    permission_required = "account.action_all"
    model = User
    template_name = "admin_panel/users/users_list.html"
    context_object_name = "users"


class AddUsersView(PermissionRequiredMixin, CreateView):
    permission_required = "account.action_all"
    form_class = UserCreationForm
    template_name = "admin_panel/users/users_create.html"
    success_url = "/admin_panel/users/"
