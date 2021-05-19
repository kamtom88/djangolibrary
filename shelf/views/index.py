from django.shortcuts import render
from ..models import book


def index(request):
    message = book.Book.objects.all().count()
    template = 'index.html'
    context = {'message': message,

               }
    return render(request, template, context)

