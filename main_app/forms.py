from django import forms
from .models import Physical, Mental, Emotional, Diary, Goals


class PhysicalForm(forms.ModelForm):
    class Meta:
        model = Physical
        fields = '__all__'
        
class MentalForm(forms.ModelForm):
    class Meta:
        model = Mental
        fields = '__all__'
       
        
        
class EmotionalForm(forms.ModelForm):
    class Meta:
        model = Emotional
        fields = '__all__'
       
       
class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = '__all__'
        