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


class TextQuestion(Question):
    form_class = forms.CharField
    max_length = models.IntegerField(default=1000)


class SelectOneQuestion(Question):
    form_class = forms.IntegerField


class Reply(models.Model):
    answers = JSONField()
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.SET_NULL, null=True)
    questionnaire_title = models.CharField(max_length=100)
