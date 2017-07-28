from django import forms
from .models import reserve


class reserveForm(forms.ModelForm):


    class Meta:
        model = reserve
        fields = ['package', 'email', 'time', 'comments', ]
        widgets = {
            'package': forms.TextInput(attrs={'class': 'form-control disabled', 'placeholder': "Package"}),
            'time': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': "Desired Date [YYYY-MM-DD]"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comments'}), }
