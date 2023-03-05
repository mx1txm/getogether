import django_filters

from django_filters import DateFilter
from .models import Post


class ListingFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    date_posted = django_filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'], lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author', lookup_expr='iexact')

    city_choices = django_filters.ChoiceFilter(field_name='city', lookup_expr='iexact')
    category = django_filters.ChoiceFilter(field_name='category', lookup_expr='iexact')
    weekday = django_filters.ChoiceFilter(field_name='weekday', lookup_expr='iexact')
    berlin_bezirk = django_filters.ChoiceFilter(field_name='bezirk', lookup_expr='iexact')


    class Meta:
        model = Post
        fields = ['title', 'city', 'category', 'weekday', 'bezirk']

