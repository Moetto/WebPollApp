from django import forms
from django.db import models
from django.contrib.postgres.fields import JSONField
from polymorphic.models import PolymorphicModel


class Questionnaire(models.Model):
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField('Question')

    def __str__(self):
        return self.title


class Question(PolymorphicModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return format(self.title)


class TextQuestion(Question):
    answer = models.TextField(max_length=1000, blank=True, null=True, name='answer')
    form_class = forms.CharField
    max_length = models.IntegerField(default=1000)


class SelectOneQuestion(Question):
    answer = models.IntegerField(blank=True, null=True, name='select_one')
    form_class = forms.IntegerField


class Reply(models.Model):
    answers = JSONField()
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.SET_NULL, null=True)
    questionnaire_title = models.CharField(max_length=100)
