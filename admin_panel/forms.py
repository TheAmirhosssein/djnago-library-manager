from django import forms

from library.models import Books

# class BooksForm(ModelForm):
#     class Meta:
#         model = Books
#         fields = "__all__"


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
            "detail": forms.TextInput(
                attrs={"class": "form-control", "label": "توضیحات کوتاه"}
            ),
            "translator": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "author": forms.Select(attrs={"class": "form-control"}),
            "publisher": forms.Select(attrs={"class": "form-control"}),
            "genres": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
