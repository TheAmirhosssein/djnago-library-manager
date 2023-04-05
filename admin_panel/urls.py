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
    path("books/filter/<author>", views.BooksListView.as_view(), name="book_author"),
    # authors
    path("authors/", views.AuthorsListView.as_view(), name="authors_admin"),
    path("authors/create/", views.AddAuthorsView.as_view(), name="authors_create"),
    path(
        "authors/<pk>/update/", views.UpdateAuthorView.as_view(), name="author_update"
    ),
    path(
        "authors/<pk>/delete/", views.DeleteAuthorView.as_view(), name="author_delete"
    ),
    path("authors/search/", views.SearchAuthorView.as_view(), name="author_search"),
    # publishers
    path("publishers/", views.PublishersListView.as_view(), name="publishers_admin"),
    path(
        "publishers/create/",
        views.AddPublishersView.as_view(),
        name="publishers_create",
    ),
    path(
        "publishers/<pk>/update/",
        views.UpdatePublisherView.as_view(),
        name="publisher_update",
    ),
    path(
        "publishers/<pk>/delete/",
        views.DeletePublisherView.as_view(),
        name="publisher_delete",
    ),
    path(
        "publishers/search/",
        views.SearchPublishersView.as_view(),
        name="publisher_search",
    ),
    # translators
    path("translators/", views.TranslatorListView.as_view(), name="translators_admin"),
    path(
        "translators/create/",
        views.AddTranslatorView.as_view(),
        name="translators_create",
    ),
    path(
        "translators/<pk>/update",
        views.UpdateTranslatorView.as_view(),
        name="translator_update",
    ),
    path(
        "translators/<pk>/delete/",
        views.DeleteTranslatorView.as_view(),
        name="translator_delete",
    ),
    path(
        "translators/search/",
        views.SearchTranslatorsView.as_view(),
        name="translator_search",
    ),
    # genres
    path("genres/", views.GenresListView.as_view(), name="genres_admin"),
    path("genres/create/", views.AddGenresView.as_view(), name="genres_create"),
    path("genres/<pk>/update/", views.UpdateGenresView.as_view(), name="genre_update"),
    path("genres/<pk>/delete/", views.DeleteGenreView.as_view(), name="genre_delete"),
    path("genres/search/", views.SearchGenresView.as_view(), name="genre_search"),
    # users
    path(
        "users/",
        views.UsersListView.as_view(),
        name="users_admin",
    ),
    path("users/create/", views.AddUsersView.as_view(), name="users_create"),
    path("users/<pk>/update/", views.UpdateUserView.as_view(), name="user_update"),
    path("users/<pk>/delete/", views.DeleteUserView.as_view(), name="user_delete"),
    path("users/search/", views.SearchUsersView.as_view(), name="user_search"),
]
