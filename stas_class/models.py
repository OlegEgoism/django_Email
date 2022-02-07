from django.db import models


class Zawod(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название завода')
    address = models.CharField(max_length=200, verbose_name="Адрес")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Стоимость')
    zawod = models.ForeignKey('Zawod', on_delete=models.CASCADE)

    def __str__(self):
        return self.name