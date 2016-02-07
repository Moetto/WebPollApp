from collections import OrderedDict

from django import forms
from django.db import models
from django.contrib.postgres.fields import JSONField
from polymorphic.models import PolymorphicModel
from sortedm2m.fields import SortedManyToManyField


class Questionnaire(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000, blank=True, null=True)
    questions = SortedManyToManyField('Question')

    def __str__(self):
        return self.title


class Question(PolymorphicModel):
    help_text = models.TextField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return format(self.title)

    def field_kwargs(self):
        return {'help_text': self.help_text}


class TextQuestion(Question):
    form_class = forms.CharField
    max_length = models.IntegerField(default=1000)

    def get_field(self, **kwargs):
        return self.form_class(**self.field_kwargs())

    def field_kwargs(self):
        kw = super().field_kwargs()
        kw['max_length'] = self.max_length
        return kw


class SelectOneQuestion(Question):
    form_class = forms.ChoiceField
    widget_classes = OrderedDict([('default', forms.Select,), ('radio button', forms.RadioSelect,)])
    widget_choices = [(key, key,) for key in widget_classes.keys()]
    widget = models.CharField(max_length=20, choices=widget_choices, default='default')

    options = models.ManyToManyField('SelectOption')

    def get_field(self, **kwargs):
        choices = [(option, option,) for option in self.options.all()]
        return self.form_class(choices=choices, **self.field_kwargs())

    def field_kwargs(self):
        kw = super().field_kwargs()
        kw['widget'] = self.widget_classes[self.widget]
        return kw


class SelectOption(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Reply(models.Model):
    class Meta:
        verbose_name_plural = 'Replies'

    answers = JSONField()
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.SET_NULL, null=True)
    questionnaire_title = models.CharField(max_length=100)

    def __str__(self):
        if self.questionnaire is not None:
            return self.questionnaire.title
        return "Reply"
