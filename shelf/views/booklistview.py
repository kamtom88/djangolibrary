from django.views.generic import ListView

from ..models import book


class BookListView(ListView):
    model = book.Book
