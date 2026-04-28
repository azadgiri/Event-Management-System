from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['attendee_name', 'attendee_email']
        widgets = {
            'attendee_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Name'}),
            'attendee_email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email'}),
        }
