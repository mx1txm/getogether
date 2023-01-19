from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Author(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.CharField(max_length=100, default='SOME STRING')
    print("Post Model")

    category_choices = (
        ('Kunst', 'Kunst'),
        ('Bildung', 'Bildung'),
        ('Kultur', 'Kultur'),
        ('Musik', 'Musik'),
        ('Umwelt', 'Umwelt'),
        ('Zusammenkommen', 'Zusammenkommen'),
        ('Kiezgestaltung', 'Kiezgestaltung'),
        ('Tanzen', 'Tanzen'),
        ('Essen', 'Essen'),
    )

    city_choices = (
        ('Berlin', 'Berlin'),
        ('Bielefeld', 'Bielefeld'),
        ('Frankfurt', 'Frankfurt'),
        ('München', 'München'),
        ('Hamburg', 'Hamburg'),
        ('Köln', 'Köln'),
    )

    weekday_choices = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    category = models.CharField(max_length=15, choices=category_choices, default=0)
    city = models.CharField(max_length=15, choices=city_choices, default=0)
    weekday = models.CharField(max_length=15, choices=weekday_choices, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
