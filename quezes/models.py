from django.db import models
from questions.models import Question

class Quiz(models.Model):
    number = models.IntegerField(verbose_name='Опрос № ', max_length=2)
    desc = models.TextField(verbose_name='Описание')
    questions = models.ForeignKey(Question, verbose_name='Вопросы')
