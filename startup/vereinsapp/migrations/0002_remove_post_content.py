# Generated by Django 4.1 on 2023-01-12 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vereinsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
