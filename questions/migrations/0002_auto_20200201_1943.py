# Generated by Django 2.2.9 on 2020-02-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(verbose_name='Вопрос'),
        ),
    ]
