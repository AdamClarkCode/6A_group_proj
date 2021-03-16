from django.shortcuts import render
from django.http import HttpResponse
from rango.forms import StoryForm
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def add_story(request):
    form = StoryForm()
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/story/')
        else:
            print(form.errors)
    return render(request, 'story/add_story.html', {'form': form})