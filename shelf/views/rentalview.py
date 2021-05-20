from django.views.generic import TemplateView,FormView
from django.shortcuts import render
from ..models import rental
from ..forms import RentalForm


class RentalView(FormView):
    template_name = 'shelf/rental.html'
    form_class = RentalForm
    success_url = '/'