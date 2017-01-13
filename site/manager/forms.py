from django import forms
from .models import employee


class addEmployee(forms.ModelForm):

    class Meta:
        model = employee
        fields = '__all__'
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'wage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wage'}),}


