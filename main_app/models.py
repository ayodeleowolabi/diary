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
    location = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f' {self.user} is at {self.location} on {self.date}'
    
    def get_absolute_url(self):
        return reverse("diary-detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['date']



class Images(models.Model):
    image1 = models.ImageField(default='', upload_to='images/')
    diary_key = models.ForeignKey(Diary, on_delete=models.CASCADE)

class DynamicChoiceField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.user_choices = []
        super().__init__(*args, **kwargs)

    def get_choices(self, include_blank=True, blank_choice=None, **kwargs):
        # Logic to fetch user-specific choices dynamically
        return self.user_choices




class Goals(models.Model):
   goal = DynamicChoiceField(max_length=100)


class Physical(models.Model):
    breakfast_check = models.BooleanField(default=False)
    breakfast = models.CharField(max_length=100)
    lunch = models.CharField(max_length=100)
    dinner = models.CharField(max_length=100)
    snacks = models.CharField(max_length=100)
    exercise = models.BooleanField(default=False)
    body_part_worked = models.CharField()
    workout_link = models.TextField("")
    diary_key = models.ForeignKey(Diary, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Breakfast: {self.breakfast}, Lunch: {self.lunch}, Dinner: {self.dinner}, Snacks: {self.snacks}'
    
    
class Mental(models.Model):
    meditation = models.BooleanField(default=False)
    time_spent = models.IntegerField(default=0)
    fears = models.TextField(max_length=100)
    desires = models.TextField(max_length=100)
    learning_goals = models.ForeignKey(Goals, on_delete=models.CASCADE)
    diary_key = models.ForeignKey(Diary, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Time Spent: {self.time_spent},Fears: {self.fears}, Desires: {self.desires}'
    
    
    
class Emotional(models.Model):
    community_check = models.BooleanField(default=False)
    community_activities = models.CharField()
    time_spent = models.IntegerField(default=0)
    gratitude_list = models.TextField()
    vices = models.TextField("")
    drink = models.BooleanField(default=False)
    number_of_drinks = models.IntegerField(default=0)
    morning_mood = models.CharField(
        choices=MOOD,
        default=MOOD[0][0]
    )
    diary_key = models.ForeignKey(Diary, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Activities: {self.community_activities}, Vices: {self.vices}'
    
    