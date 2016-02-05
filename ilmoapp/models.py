from django.db import models
from polymorphic.models import PolymorphicModel


class QuestionForm(models.Model):
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField('Question')

    def __str__(self):
        return self.title


class Question(PolymorphicModel):
    title = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class TextQuestion(Question):
    answer = models.TextField(max_length=1000, blank=True, null=True)


class SelectOneQuestion(Question):
    answer = models.IntegerField(blank=True, null=True)
