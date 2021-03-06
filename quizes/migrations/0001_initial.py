# Generated by Django 2.2.9 on 2020-02-02 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Опрос № ')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='questions.Question', verbose_name='Вопросы')),
            ],
        ),
    ]
