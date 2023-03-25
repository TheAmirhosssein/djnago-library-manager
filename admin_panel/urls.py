from django.urls import path

from admin_panel import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="admin"),
    path("books/", views.BooksListView.as_view(), name="books_admin"),
    path("books/create/", views.AddBookView.as_view(), name="books_create"),
]
