from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.forms import formset_factory
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accaunt.forms import BookForm
from accaunt.serializers import UserRegisterationsSerializer


class ApiUserRegistartionView(APIView):
    def post(self, request):
        serializer = UserRegisterationsSerializer(data=request.data)
        if serializer.is_valid():
            password1 = serializer.validated_data.get('password')
            password2 = serializer.validated_data.get('password')
            if password1 == password2:
                username = serializer.validated_data.get('username')
                email = serializer.validated_data.get('email')
                serializer.save()
                # print(int)
                # new_user = User.objects.create_user(username=username, email=email)
                # serializer.save(username=username, password=password1, email=email)
            print(serializer.validated_data)
            return Response(serializer.data)




    def get(self, request):
        user = User.objects.all()
        serializer = UserRegisterationsSerializer(user, many=True)
        return Response(serializer.data)

@receiver(pre_save, sender=User)
def my_handler(sender, **kwargs):
    print('сингнал оК')

    send_mail(
        'Регистрация',
        'Ваш новый аккаунт.',
        'vp3231963@gmail.com',
        ['olegpustovalov220@gmail.com'],
        fail_silently=False,
    )


class SimpleApI(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



def book(request):
    return render(request, template_name='home.html', context={'formset': formset_factory(BookForm), })














    # models = Samples
    # template_name = 'home.html'
    # context_object_name = 'samples'
    # paginate_by = 2
    #
    # def get_queryset(self):
    #     return Samples.objects.filter(published=True)
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Семплы'
    #     context['style'] = Style.objects.all()
    #     context['author'] = Author.objects.all()
    #     return context


