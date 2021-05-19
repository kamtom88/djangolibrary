from django import forms
from .models import message


class MessageForm(forms.ModelForm):
    class Meta:
        model = message.Message
        fields = ('name', 'email', 'text')