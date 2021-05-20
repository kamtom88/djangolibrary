from django import forms
from .models import message, rental


class MessageForm(forms.ModelForm):
    class Meta:
        model = message.Message
        fields = ('name', 'email', 'text')


class RentalForm(forms.ModelForm):
    class Meta:
        model = rental.Rental
        fields = ('who', 'what', 'when')
