from django import forms
from .models import contact


class contactForm(forms.ModelForm):

    class Meta:
        model = contact
        fields = ['name', 'subject', 'email', 'message', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Subject"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message...'}), }


