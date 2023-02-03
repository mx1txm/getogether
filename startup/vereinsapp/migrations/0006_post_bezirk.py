# Generated by Django 4.1 on 2023-01-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vereinsapp', '0005_remove_post_post_post_beschreibung'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bezirk',
            field=models.CharField(choices=[('Mitte', 'Mitte'), ('Friedrichshain', 'Friedrichshain'), ('Pankow', 'Pankow'), ('Charlottenburg', 'Charlottenburg'), ('Kreuzberg', 'Kreuzberg'), ('Spandau', 'Spandau'), ('Steglitz', 'Steglitz'), ('Schöneberg', 'Schöneberg'), ('Neukölln', 'Neukölln'), ('Köpenick', 'Köpenick'), ('Lichtenberg', 'Lichtenberg'), ('Marzahn', 'Marzahn')], default=0, max_length=15),
        ),
    ]
