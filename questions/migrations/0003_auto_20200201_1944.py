# Generated by Django 2.2.9 on 2020-02-01 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200201_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='answers.Answer', verbose_name='Ответы'),
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.IntegerField(verbose_name='Порядок'),
        ),
    ]
