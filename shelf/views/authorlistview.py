from django.views.generic import ListView
from ..models import author
# from Library.shelf.models import author


class AuthorListView(ListView):
    model = author.Author
