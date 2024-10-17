from django import forms
from .models import Physical, Mental, Emotional, Diary, Goals


class PhysicalForm(forms.ModelForm):
    class Meta:
        model = Physical
        fields = '__all__'
        widgets = {'physical_goals': forms.HiddenInput()}
        
class MentalForm(forms.ModelForm):
    class Meta:
        model = Mental
        fields = '__all__'
        widgets = {'learning_goals': forms.HiddenInput()}
       
       
        
        
class EmotionalForm(forms.ModelForm):
    class Meta:
        model = Emotional
        fields = '__all__'
        widgets = {'emotional_goals': forms.HiddenInput()}
       
       
class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = '__all__'
        