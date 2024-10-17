from django import forms
from .models import Physical, Mental, Emotional, Diary, Goals


class PhysicalForm(forms.ModelForm):
    class Meta:
        model = Physical
        fields = ['breakfast', 'lunch', 'dinner', 'snacks', 'exercise', 'body_part_worked', 'length_of_workout', 'workout_link']
        
class MentalForm(forms.ModelForm):
    class Meta:
        model = Mental
        fields = ['meditation', 'time_spent', 'fears', 'desires']
       
       
        
        
class EmotionalForm(forms.ModelForm):
    class Meta:
        model = Emotional
        fields = ['community_check','time_spent','community_activities' ,'gratitude_list', 'vices','drink', 'number_of_drinks', 'evening_mood' , 'morning_mood']
       
       
class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = '__all__'
        