from django.views.generic import DetailView, FormView
from ..models import message
from ..forms import MessageForm


# class MessageDetailView(DetailView):
#     model = message.Message
#

class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'shelf/contact.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(MessageAddView, self).form_valid(form)