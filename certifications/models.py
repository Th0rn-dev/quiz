from django.db import models
from questions.models import Question


class Certificate(models.Model):
    number = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    questions = models.ForeignKey(Question, on_delete=models.DO_NOTHING)