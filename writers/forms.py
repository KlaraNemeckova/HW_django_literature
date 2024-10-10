from django import forms
from .models import Book_ranking


class BookForm(forms.ModelForm):
    class Meta:
        model = Book_ranking
        fields = "__all__"