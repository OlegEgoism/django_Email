from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from svazi.forms import BookForm
from svazi.models import Book
from svazi.serializers import BookSerializer


@api_view(['GET', 'POST'])
def book(request):
    all = Book.objects.all()
    book = BookSerializer(all, many=True)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return Response(book.data)


def bo(request):
    # all = Book.objects.all()
    form = BookForm(request.POST)
    # print(form)
    if request.method == "POST":
        print(request.POST)
        # form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            render(request, template_name='bo.html')
        return render(request, template_name='bo.html')
    context = {
        'book': book,
        'form': form,
        'all': all
    }
    return render(request, template_name='bo.html', context=context)