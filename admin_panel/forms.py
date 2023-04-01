from django import forms

from library.models import Authors, Books, Genres, Publishers, Translators


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ["slug"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "book_image": forms.FileInput(
                attrs={"class": "form-control", "label": "تصویر مقاله"}
            ),
            "detail": forms.Textarea(
                attrs={"class": "form-control", "label": "توضیحات کوتاه"}
            ),
            "translator": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "author": forms.Select(attrs={"class": "form-control"}),
            "publisher": forms.Select(attrs={"class": "form-control"}),
            "book_user": forms.Select(attrs={"class": "form-control"}),
            "genres": forms.SelectMultiple(attrs={"class": "form-control"}),
        }


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Authors
        exclude = ["slug"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            )
        }


class PublishersForm(forms.ModelForm):
    class Meta:
        model = Publishers
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class TranslatorsForm(forms.ModelForm):
    class Meta:
        model = Translators
        exclude = ["slug"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            )
        }


class GenresForm(forms.ModelForm):
    class Meta:
        model = Genres
        exclude = ["slug"]
        widgets = {"title": forms.TextInput(attrs={"class": "form-control"})}
