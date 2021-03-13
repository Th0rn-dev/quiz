from django.db import models
from answers.models import Answer

# Create your models here.
class Question(models.Model):
    body = models.TextField(verbose_name="Ответ")
    order = models.IntegerField()
    answer = models.ForeignKey(Answer, on_delete=models.DO_NOTHING)