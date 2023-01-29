from django import forms
from django.forms import TextInput, Textarea, DateInput, NumberInput

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course',
                  'description', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your course'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course',
                  'description', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your course'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
