from django.urls import path

from admin_panel import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="admin"),
    # books
    path("books/", views.BooksListView.as_view(), name="books_admin"),
    path("books/create/", views.AddBookView.as_view(), name="books_create"),
    path("books/<pk>/update/", views.UpdateBookView.as_view(), name="book_update"),
    path("books/<pk>/delete/", views.DeleteBookView.as_view(), name="book_delete"),
    path("books/search/", views.SearchBookView.as_view(), name="book_search"),
    # authors
    path("authors/", views.AuthorsListView.as_view(), name="authors_admin"),
    path("authors/create/", views.AddAuthorsView.as_view(), name="authors_create"),
    path(
        "authors/<pk>/update/", views.UpdateAuthorView.as_view(), name="author_update"
    ),
]
