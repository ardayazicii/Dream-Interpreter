from django import forms
from .models import Dream

class DreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = ['title', 'description', 'interpretation']  # İhtiyaç duyduğun tüm alanlar
