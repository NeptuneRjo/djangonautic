from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    # define how we want to output the form
    # what fields do we want to be present
    # which model do we want to inherit these fields from
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']
