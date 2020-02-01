from django.db import models

class Answer(models.Model):
    body = models.CharField(max_length=200, verbose_name="Ответ")
    check = models.BooleanField(verbose_name="Проверка")
