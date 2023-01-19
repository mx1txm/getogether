from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Post
import django_filters

class FilterForm(forms.ModelForm):
    post = forms.CharField()
    author = django_filters.CharFilter(lookup_expr='iexact')
    title = django_filters.CharFilter(lookup_expr='icontains')
    #category = django_filters.CharFilter(lookup_expr='iexact') #ChoiceFilter?

    class Meta:
        model = Post
        fields = ('title', 'author')


class AnzeigeForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Post

        # specify fields to be used
        fields = [
            "title",
            "category",
            "weekday",
        ]


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        print("Inside Postform init")

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Post
        fields = ('title', 'category', 'weekday')
