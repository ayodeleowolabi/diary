from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import requests
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Diary, Physical, Mental
from django.utils import timezone
from .forms import PhysicalForm, MentalForm

# Create your views here.



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
    physical_form = PhysicalForm()
    print(diary)
    return render(request, 'diary/detail.html', {'diary': diary, 'today': today == diary.date, 'physical_form': physical_form})


def add_physical(request, diary_id):
    form = PhysicalForm(request.POST)
    if form.is_valid():
        new_physical = form.save(commit=False)
        new_physical.diary_id = diary_id
        new_physical.save()
    return redirect('diary-detail', diary_id=diary_id)

class PhysicalUpdate(UpdateView):
    model = Physical
    fields = '__all__'
    success_url = '/diary/'
    
class PhysicalDelete(DeleteView):
    model = Physical
    success_url = '/diary/'
    

def add_mental(request, diary_id):
    form = MentalForm(request.POST)
    if form.is_valid():
        new_mental = form.save(commit=False)
        new_mental.diary_id = diary_id
        new_mental.save()
    return redirect('diary-detail', diary_id=diary_id)

def home(request):
    diary = Diary.objects.filter(user=request.user)
    response = requests.get('https://zenquotes.io/api/random/q')
    quote = response.json()[0]['q']
    author = response.json()[0]['a']
    print(quote)
    return render(request, 'home.html', {'q': quote, 'a': author, 'diary': diary})
