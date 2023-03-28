from django.urls import path

from admin_panel import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="admin"),
    path("books/", views.BooksListView.as_view(), name="books_admin"),
    path("books/create/", views.AddBookView.as_view(), name="books_create"),
    path("books/<pk>/update/", views.UpdateBookView.as_view(), name="book_update"),
    path("books/<pk>/delete/", views.DeleteBookView.as_view(), name="book_delete"),
]
