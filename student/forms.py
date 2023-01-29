from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'is_olympic', 'email', 'trainer', 'gender',
                  'description', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control','placeholder':'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first email'}),
            'trainer': Select(attrs={'class': 'form-select'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    def clean(self):
        cleaned_data = self.cleaned_data
        get_email = cleaned_data.get('email')  # cleaned_data['email']
        all_students = Student.objects.all()
        for student in all_students:
            if get_email == student.email:
                msg = f'This email {get_email} exists already in the databases.'
                self._errors['email'] = self.error_class([msg])
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        for student in all_students:
            if start_date > end_date:
                message = f'The start data {start_date} is after the date of {end_date} '
                self._errors['start_date'] = self.error_class([message])
        return cleaned_data

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'is_olympic', 'email', 'trainer', 'gender',
                  'description', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control','placeholder':'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first email'}),
            'trainer': Select(attrs={'class': 'form-select'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }