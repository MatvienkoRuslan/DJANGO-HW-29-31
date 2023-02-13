from django import forms
from .models import *


class TaskForm(forms.Form):
    title = forms.CharField(max_length=255, label="Task Title")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Description')
    completed = forms.BooleanField(required=False, initial=True, label='Completed')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category')

