from django import forms
from django.conf import settings


class WordCountForm(forms.Form):
    """Form for word counting."""

    text = forms.CharField(
        label='',
        max_length=settings.MAX_TEXT_SIZE,
        widget=forms.Textarea(attrs={'cols':80, 'rows':20}),
    )
