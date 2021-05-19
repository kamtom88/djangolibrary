from django.views.generic import ListView

from ..models import publisher


class PublisherListView(ListView):
    model = publisher.Publisher
