from django.db import models
from questions.models import Question

class Quiz(models.Model):
    number = models.IntegerField(verbose_name='Опрос № ')
    desc = models.TextField(verbose_name='Описание')
    questions = models.ForeignKey(Question, verbose_name='Вопросы', on_delete=models.DO_NOTHING)
