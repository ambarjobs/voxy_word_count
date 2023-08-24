from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View

from main.business_rules import word_counter
from main.forms import WordCountForm

class WordCount(View):
    def get(self, request):
        """Page rendering."""

        template_name = 'main.html'
        form = WordCountForm()
        return render(request, template_name=template_name, context={'word_count_form': form})

    def post(self, request):
        """Form processing."""

        form = WordCountForm(request.POST)
        if form.is_valid():
            count = word_counter(form.cleaned_data['text'])
            plural = 's' if count != 1 else ''
            messages.add_message(request, messages.SUCCESS, f'You typed {count} word{plural}.')
        else:
            for error in form.errors.values():
                messages.add_message(request, messages.ERROR, error.as_text())
        return redirect('main.word_count')
