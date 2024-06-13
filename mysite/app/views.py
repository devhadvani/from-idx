from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h1>About Us</h1>")


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Story
from .forms import StoryForm,LoginForm

@login_required
def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.expires_at = timezone.now() + timezone.timedelta(days=1)  # Expires in 24 hours
            story.save()
            return redirect('view_story')
    else:
        form = StoryForm()
    return render(request, 'create_story.html', {'form': form})

@login_required
def view_story(request):
    stories = Story.objects.filter(user=request.user)
    print(stories)
    return render(request, 'view_story.html', {'stories': stories})

@login_required
def delete_story(request, story_id):
    story = Story.objects.get(pk=story_id)
    if story.user == request.user:
        story.delete()
    return redirect('view_story')



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
