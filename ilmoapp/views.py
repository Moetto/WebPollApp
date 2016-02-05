import json

from django import forms
from django.views.generic import View, FormView
from django.shortcuts import render, get_object_or_404

from ilmoapp.models import *


class QuestionForm(FormView):
    def get_form(self, form_class=None):
        class Form(forms.Form):
            def __init__(self, form_id, *args, **kwargs):
                super().__init__(*args, **kwargs)
                questionnaire = get_object_or_404(Questionnaire, id=form_id)
                for question in questionnaire.questions.all():
                    field = question.form_class(help_text=question.help_text)
                    self.fields[question.title] = field

        return Form(form_id=self.kwargs['id'], **self.get_form_kwargs())

    success_url = '/'
    template_name = 'ilmoapp/basictemplate.html'

    def form_valid(self, form):
        questionnaire = get_object_or_404(Questionnaire, id=self.kwargs['id'])
        answers = {}
        for field in form.cleaned_data.keys():
            answers[field] = form.cleaned_data[field]
        Reply(questionnaire=questionnaire, questionnaire_title=questionnaire.title, answers=answers).save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questionnaire'] = get_object_or_404(Questionnaire, id=self.kwargs['id'])
        return context
