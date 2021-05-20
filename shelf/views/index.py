from django.shortcuts import render
from ..models import book
from django.views.generic import TemplateView
#
# def index(request):
#     message = book.Book.objects.all().count()
#     template = 'index.html'
#     context = {'message': message,
#
#                }
#     return render(request, template, context)
#


class MainPage(TemplateView):
    template_name = 'index.html'

    def get(self,request, *args, **kwargs):
        message = book.Book.objects.all().count()
        template = 'index.html'
        context = {'message': message,

                   }
        return render(request, template, context)
#
