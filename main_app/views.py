from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import requests
from django.contrib.auth.views import LoginView
from .models import Diary
from django.utils import timezone

# Create your views here.

class Home(LoginView):
    template_name = 'home.html'


def signup(request):
    error_message=""
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


def diary_index(request):
    today = timezone.now().date()
    diary = Diary.objects.filter(date=today, user=request.user)
    if not diary: 
        diary = Diary.objects.create(user=request.user, date=today)   
    diarys = Diary.objects.all()
    return render(request, 'diary/index.html', {'diarys': diarys})

def diary_detail(request, diary_id):
    today = timezone.now().date()
    diary = Diary.objects.get(id=diary_id)
    print(diary)
    return render(request, 'diary/detail.html', {'diarys': diary, 'today': today == diary.date})