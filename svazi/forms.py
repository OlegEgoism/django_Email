from django import forms
from .models import *


class BookForm(forms.ModelForm):
    # name = forms.CharField(max_length=250, label='Имя')
    # price = forms.DecimalField(max_digits=8, decimal_places=2, label='Цена')
    # author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), label='Автор')
    # genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label=':Жанры')

    class Meta:
        model = Book
        fields = '__all__'


    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #
    # user.set_password(self.cleaned_data['password1'])
    # user.is_active = False
    # user.is_activated = False
    # if commit:
    #     user.save()
    # # user_registered.send(UserRegisterForm, instance=user)
    # return user

    # def create(self, validated_data):
   #      author = validated_data.pop('author')
   #      genre = validated_data.pop('genre')
   #      author_id, s = Author.objects.get_or_create(**author)
   #      book_id = Book.objects.create(author=author_id, **validated_data)
   #      for i in genre:
   #          genrename = i['name']
   #          generobj, s = Genre.objects.get_or_create(name=genrename)
   #          book_id.genre.add(generobj)
   #          print(generobj)
   #      return book_id



        # exclude = ['genre', ]


# class GenreForm(forms.ModelForm):
#     class Meta:
#         model = Genre
#         fields = '__all__'
#
#
