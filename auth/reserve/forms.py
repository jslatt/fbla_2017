from django import forms
from .models import reserve


class reserveForm(forms.ModelForm):

    class Meta:
        model = reserve
        fields = ['package', 'time', 'comments', ]
        CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'),)
        widgets = {
            'package': forms.ChoiceField(choices=CHOICES, attrs={'class': 'form-control', }),
            'time': forms.DateTimeField(attrs={'class': 'form-control', }),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comments'}),
        }

