from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره تلفن',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع خود را وارد کنید',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'لطفا جزئیات را بنویسید',
                'rows': 3,
            }),
        }
