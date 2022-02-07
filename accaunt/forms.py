from django import forms
from .models import *


class BookForm(forms.ModelForm):
    # name = forms.CharField(max_length=250, label='Имя')
    # price = forms.DecimalField(max_digits=8, decimal_places=3, label='Цена')
    # author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), label='Автор')
    # genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label=':Жанры')

    class Meta:
        model = Book
        exclude = ['genre', ]
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

