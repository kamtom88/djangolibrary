from django.views.generic import DetailView
from ..models import author
# from Library.Library.shelf.models import author


class AuthorDetailView(DetailView):
    model = author.Author
#
