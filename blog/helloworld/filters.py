import django_filters
from django import forms
from .models import Post

class PostFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=Post.STATUS_CHOICES)
    created_on = django_filters.DateTimeFilter(widget = forms.DateInput(attrs={"type":"date"}),lookup_expr="date__exact")
    updated_on = django_filters.DateTimeFilter(widget = forms.DateInput(attrs={"type":"date"}),lookup_expr="date__exact")


    class Meta:
        model = Post
        fields = ['created_on','updated_on','status']