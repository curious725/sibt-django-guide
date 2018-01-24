from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
        help_texts = {
            'subject': _('The max length of the text is 255.'),
        }
