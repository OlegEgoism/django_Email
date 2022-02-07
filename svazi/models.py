from django.db import models


class Author(models.Model):
    name = models.CharField('Автор', max_length=250)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Жанры', max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre', related_name='genre')

    def __str__(self):
        return self.name
