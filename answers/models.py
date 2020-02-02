from django.db import models

class Answer(models.Model):
    body = models.TextField(max_length=200, verbose_name="Ответ")
    check = models.BooleanField(verbose_name="Проверка")
