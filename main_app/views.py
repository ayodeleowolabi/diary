import os
from django.shortcuts import render, redirect
import uuid
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
import requests
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Diary, Physical, Mental, Emotional, Photo
from django.utils import timezone
from .forms import PhysicalForm, MentalForm, EmotionalForm
import boto3

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


@login_required
def diary_index(request):
    today = timezone.now().date()
    diary = Diary.objects.filter(date=today, user=request.user)
    if not diary: 
        diary = Diary.objects.create(user=request.user, date=today)   
    diarys = Diary.objects.all()
    return render(request, 'diary/index.html', {'diarys': diarys})

@login_required
def diary_detail(request, diary_id):
    today = timezone.now().date()
    diary = Diary.objects.get(id=diary_id)
    physical_form = PhysicalForm()
    mental_form = MentalForm()
    emotional_form = EmotionalForm()
    print(diary_id)
    return render(request, 'diary/detail.html', {'diary': diary, 'today': today == diary.date, 'physical_form': physical_form, 'mental_form': mental_form, 'emotional_form': emotional_form})

@login_required
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



class MentalUpdate(UpdateView):
    model = Mental
    fields = '__all__'
    success_url = '/diary/'




class MentalDelete(DeleteView):
    model = Mental
    success_url = '/diary/'


@login_required
def add_emotional(request, diary_id):
    form = EmotionalForm(request.POST)
    if form.is_valid():
        new_emotional = form.save(commit=False)
        new_emotional.diary_id = diary_id
        new_emotional.save()
    return redirect('diary-detail', diary_id=diary_id)




class EmotionalUpdate(UpdateView):
    model = Emotional
    fields = '__all__'
    success_url = '/diary/'



class EmotionalDelete(DeleteView):
    model = Emotional
    success_url = '/diary/'
    
    

    
@login_required
def home(request):
        diary = Diary.objects.filter(user=request.user)
        response = requests.get('https://zenquotes.io/api/random/q')
        quote = response.json()[0]['q']
        author = response.json()[0]['a']
        print(quote)
        return render(request, 'home.html', {'q': quote, 'a': author, 'diary': diary})

        


def add_photo(request, diary_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):] 
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload.fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, diary_id=diary_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', diary_id=diary_id)