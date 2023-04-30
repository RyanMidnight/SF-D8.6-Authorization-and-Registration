from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):

    pub_date = DateFilter(
        field_name='pub_date',
        lookup_expr='gt',
        label='News published later than:',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )

    class Meta:
        model = Post
        fields = {
            'headline': ['icontains'],
            'author__name': ['icontains'],
        }
