from .views import *
from django.urls import path
from .import views


urlpatterns = [
    path('api/hello', SimpleApI.as_view()),
    path('accaunt', ApiUserRegistartionView.as_view(), name='accaunt'),
    path('home/', book, name='home'),

]
