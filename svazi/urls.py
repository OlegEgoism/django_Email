from django.urls import path

from .views import *

urlpatterns = [
    path('', book, name='book'),
    path('bo/', bo, name='bo'),
]