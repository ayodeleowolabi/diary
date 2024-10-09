from django import forms
from .models import Physical


class PhysicalForm(forms.ModelForm):
    class Meta:
        model = Physical
        fields = '__all__'