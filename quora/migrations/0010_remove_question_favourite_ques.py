# Generated by Django 3.0.8 on 2023-07-27 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0009_auto_20200920_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='favourite_ques',
        ),
    ]