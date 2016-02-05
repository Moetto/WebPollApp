from django.db import models


class Question(models.Model):
    title = models.TextField(max_length=100)
