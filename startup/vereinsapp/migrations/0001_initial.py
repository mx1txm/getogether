# Generated by Django 4.1 on 2022-11-16 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(default='SOME STRING')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.CharField(default='SOME STRING', max_length=100)),
                ('category', models.CharField(choices=[('Kunst', 'Kunst'), ('Bildung', 'Bildung'), ('Kultur', 'Kultur'), ('Musik', 'Musik'), ('Umwelt', 'Umwelt'), ('Zusammenkommen', 'Zusammenkommen'), ('Kiezgestaltung', 'Kiezgestaltung'), ('Tanzen', 'Tanzen'), ('Essen', 'Essen')], default=0, max_length=15)),
                ('city', models.CharField(choices=[('Berlin', 'Berlin'), ('Bielefeld', 'Bielefeld'), ('Frankfurt', 'Frankfurt'), ('München', 'München'), ('Hamburg', 'Hamburg'), ('Köln', 'Köln')], default=0, max_length=15)),
                ('weekday', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=0, max_length=15)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
