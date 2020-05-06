from django import forms
from . import models


class AddComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']
