from django import forms
from .models import Post
import django_filters

class FilterForm(forms.ModelForm):
    post = forms.CharField()
    author = django_filters.CharFilter(lookup_expr='iexact')
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='iexact') #ChoiceFilter?

    class Meta:
        model = Post
        fields = ('title', 'author')
