from django.views.generic import DetailView
from ..models import book
# from Library.Library.shelf.models import author


class BookDetailView(DetailView):
    model = book.Book
