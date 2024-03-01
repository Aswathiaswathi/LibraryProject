from django import forms
from . models import library
class bookform(forms.ModelForm):
    class Meta:
        model = library
        fields = '__all__'
