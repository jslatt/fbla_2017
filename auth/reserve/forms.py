from django import forms
from .models import reserve


class reserveForm(forms.ModelForm):
    PACKAGES = {
        ('MA', 'Movie Adict -- $50'),
        ('FP', 'Family Plan -- $100'),
        ('LN', 'Lazer Night - $80'),
    }

    package = forms.ChoiceField(choices=PACKAGES, required=True)

    class Meta:
        model = reserve
        fields = ['package', 'email', 'time', 'comments', ]
        widgets = {
            'time': forms.DateInput(attrs={'class': 'form-control datepicker pwidget', 'placeholder': "Time"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comments'}), }
