from django import forms
from .models import Physical, Mental


class PhysicalForm(forms.ModelForm):
    class Meta:
        model = Physical
        fields = '__all__'
        
class MentalForm(forms.ModelForm):
    class Meta:
        model = Mental
        fields = '__all__'
       
        
