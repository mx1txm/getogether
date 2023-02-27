from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Fieldset, Row, Column
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
            Fieldset(
                'Anzeige Details',
                Div(
                    Div('title', css_class='col-md-6 mb-0'),
                    Div('beschreibung', css_class='col-md-6 mb-0'),
                    css_class='row'
                ),
                Div(
                    Div('category', css_class='col-md-6 mb-0'),
                    Div('image', css_class='col-md-6 mb-0'),
                    css_class='row'
                ),
            ),
            Fieldset(
                'Anzeige Ort und Zeit',
                Div(
                    Div('city', css_class='col-md-4 mb-0'),
                    Div('bezirk', css_class='col-md-4 mb-0'),
                    Div('weekday', css_class='col-md-4 mb-0'),
                    css_class='row'
                ),
            ),
            Submit('save', 'save')
        )
        self.helper.layout.append(Submit('save', 'save'))
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Post
        fields = ('title', 'beschreibung', 'category', 'city', 'bezirk', 'weekday', 'titelbild')
