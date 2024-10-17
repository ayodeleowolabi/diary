from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User

# Create your models here.
MOOD = (
    ('H', 'Happy'),
    ('O', 'Okay'),
    ('D', 'Down'),
    ('S', 'Sad') 
)


class Diary(models.Model):
    date = models.DateField('Entry Date')
    location = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f' {self.user} is at {self.location} on {self.date}'
    
    def get_absolute_url(self):
        return reverse("diary-detail", kwargs={"pk": self.id})
    
    class Meta:
        ordering = ['date']



class Images(models.Model):
    image1 = models.ImageField(default='', upload_to='images/',blank=True, null=True )
    diary_key = models.ForeignKey(Diary, on_delete=models.CASCADE)

class DynamicChoiceField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.user_choices = []
        super().__init__(*args, **kwargs)

    def get_choices(self, include_blank=True, blank_choice=None, **kwargs):
        # Logic to fetch user-specific choices dynamically
        return self.user_choices




class Goals(models.Model):
   goal = DynamicChoiceField(max_length=100, blank=True, null=True)
   def __str__(self):
        return self.goal if self.goal else 'No Goal'


class Physical(models.Model):
    breakfast = models.CharField(max_length=100, blank=True, null=True)
    lunch = models.CharField(max_length=100, blank=True, null=True)
    dinner = models.CharField(max_length=100, blank=True, null=True)
    snacks = models.TextField(max_length=100, blank=True, null=True)
    exercise = models.BooleanField(default=False, blank=True, null=True)
    body_part_worked = models.CharField(blank=True, null=True)
    length_of_workout = models.IntegerField(default=0, blank=True, null=True)
    physical_goals = models.ForeignKey(Goals, on_delete=models.CASCADE, blank=True, null=True)
    workout_link = models.TextField('Type of Workout', blank=True, null=True)
    diary_key = models.ForeignKey(Diary, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f'Breakfast: {self.breakfast}, Lunch: {self.lunch}, Dinner: {self.dinner}, Snacks: {self.snacks}'
    
   
    
class Mental(models.Model):
    meditation = models.BooleanField(default=False, blank=True, null=True)
    time_spent = models.IntegerField(default=0, blank=True, null=True)
    fears = models.TextField(max_length=100, blank=True, null=True)
    desires = models.TextField(max_length=100, blank=True, null=True)
    learning_goals = models.ForeignKey(Goals, on_delete=models.CASCADE, blank=True, null=True)
    diary_key = models.ForeignKey(Diary, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Time Spent: {self.time_spent},Fears: {self.fears}, Desires: {self.desires}'
    
    
    
class Emotional(models.Model):
    community_check = models.BooleanField(default=False, blank=True, null=True)
    time_spent = models.IntegerField(default=0, blank=True, null=True)
    community_activities = models.CharField(blank=True, null=True)
    gratitude_list = models.TextField(blank=True, null=True)
    vices = models.TextField("", blank=True, null=True)
    drink = models.BooleanField(default=False, blank=True, null=True)
    number_of_drinks = models.IntegerField(default=0, blank=True, null=True)
    emotional_goals = models.ForeignKey(Goals, on_delete=models.CASCADE, blank=True, null=True)
    evening_mood = models.CharField(
        choices=MOOD,
        default=MOOD[0][0],
        blank=True, 
        null=True
    )
    morning_mood = models.CharField(
        choices=MOOD,
        default=MOOD[0][0],
        blank=True, 
        null=True
    )
    diary_key = models.ForeignKey(Diary, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Activities: {self.community_activities}, Vices: {self.vices}'
    
    
class Photo(models.Model):
    url=models.CharField(max_length=200)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    def __str__(self):
        return f"Photo for diary_id:' {self.diary_id} @{self.url}"