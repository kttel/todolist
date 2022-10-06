from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length="100", widget=forms.TextInput(attrs={'class': 'form-input fixed-width',
                                                                          'placeholder': 'Enter your title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 5, 'class': 'form-textarea',
                                                               'placeholder': 'Enter related description'}))
    done = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'done']