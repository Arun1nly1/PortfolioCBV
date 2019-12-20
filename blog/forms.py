from django import forms
from . import models


class Blog_entryForm(forms.ModelForm):

    class Meta:
        model = models.Blog
        fields = ("title", "pub_date", "body", "image")
        labels = {
            'pub_date': 'Publication Date',
           
        }