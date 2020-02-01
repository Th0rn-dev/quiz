from django.db import models
from answers.models import Answer

# Create your models here.
class Question(models.Model):
    body = models.TextField(verbose_name="Вопрос")
    order = models.IntegerField(verbose_name="Порядок")
    answer = models.ForeignKey(Answer, on_delete=models.DO_NOTHING, verbose_name="Ответы")