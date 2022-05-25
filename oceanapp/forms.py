from django import forms
from .models import accured 

CATEGORIES = (
    ('html', 'Html'),
    ('css', 'Css'),
    ('javascript', 'Javascript'),
    ('python', 'Python')
)

class accform(forms.ModelForm):
    class Meta:
        model= accured
        fields = ('user', 'value')

        labels = {
            'user', 
            'value'
        }

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User'}),

        }