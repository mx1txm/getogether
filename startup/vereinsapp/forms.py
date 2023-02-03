from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field
from django import forms
from .models import Post
import django_filters


class FilterForm(forms.Form):
    title = django_filters.CharFilter(lookup_expr='icontains')
    beschreibung = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.ChoiceFilter(choices=Post.city_choices)
    bezirk = django_filters.ChoiceFilter(choices=Post.berlin_bezirk)
    category = django_filters.ChoiceFilter(choices=Post.category_choices)
    weekday = django_filters.ChoiceFilter(choices=Post.weekday_choices)


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        # You can dynamically adjust your layout
        self.helper.layout = Layout(
            Div(
                Div('title', css_class='col-6'),
                Div('beschreibung', css_class='col-6'),
            ),
            Div(
                Div('city', css_class='col-6'),
                Div('bezirk', css_class='col-6'),
                Div('category', css_class='col-6'),
                Div('weekday', css_class='col-6'),
            ),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
        #self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Post
        fields = ('title', 'beschreibung', 'category', 'city', 'bezirk', 'weekday', 'titelbild')
