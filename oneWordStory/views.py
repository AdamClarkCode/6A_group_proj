from django.shortcuts import render, redirect
from django.http import HttpResponse
from oneWordStory.forms import StoryForm, UserForm, UserProfileForm, WordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from oneWordStory.models import Story, UserProfile, Word
from datetime import datetime
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))

    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).seconds > 86400:
        visits = visits + 1

        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits


def home(request):
    story_list = Story.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['featuredStories'] = story_list

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    response = render(request, 'home.html', context=context_dict)

    return response

def search(request):
    story_list = None
    #If the user has searched for something, return the relevant list
    #Otherwise the search page will be blank other than the search bar
    if request.method == 'GET' and 's' in request.GET:
        s = request.GET['s']
        if s:
            story_list = Story.objects.filter(title__contains=s)
    
    context_dict = {}
    context_dict['results'] = story_list

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    response = render(request, 'search.html', context=context_dict)

    return response

def add_story(request):
    form = StoryForm()
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            #We create a new story entry in the database, but don't commit until all of the fields are populated
            story = form.save(commit=False)
            story.author = UserProfile.objects.get(user = request.user)
            stories = Story.objects.all()
            #If the story's title is already in use, redirect the user and discard the new entry
            for s in stories:
                if(s.title == story.title):
                    messages.warning(request, 'Sorry, that story name is unavailable')
                    return redirect(request.path_info)
            #If not, save the entry to the database
            story.save()
            #and redirect them to their new story
            return redirect('oneWordStory:show_story', story.slug)
        else:
            print(form.errors)
    return render(request, 'story/add_story.html', {'form': form})
    

def show_story(request, story_name_slug):
    form = WordForm()
    #If they've submitted a new word to add to the story
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            #Add a new word entry to the database with the appropriate attributes
            word = form.save(commit=False)
            word.userProfile = UserProfile.objects.get(user = request.user)
            word.story = Story.objects.get(slug=story_name_slug)
            story = Story.objects.get(slug=story_name_slug)
            
            #Prevent the user from submitting multiple words in a row
            if(word.userProfile == story.lastUser):
                messages.warning(request, 'You cannot enter two words in a row')
                return redirect('oneWordStory:show_story', story_name_slug)
                
            story.lastUser = word.userProfile
            story.save()
            word.save()
            return redirect('oneWordStory:show_story', story_name_slug)
        else:
            print(form.errors)
            messages.warning(request, 'Input is invalid, only input one word')
            return redirect('oneWordStory:show_story', story_name_slug)
    
    #If they're just viewing the story
    else:
        context_dict = {}
        try:
            story = Story.objects.get(slug=story_name_slug)
            #The words automatically sort by when they were added
            words = Word.objects.filter(story=story)
            
            context_dict['story'] = story
            context_dict['words'] = words
            context_dict['form'] = form
        except Story.DoesNotExist:
            context_dict['story'] = None
            context_dict['words'] = None
            context_dict['form'] = None
        return render(request, 'story/story.html', context = context_dict)
    
def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Changes to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, process form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Hash the password with the set_password method, then update user object.
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # Put user picture in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Save the UserProfile model instance.
            profile.save()

            # Template registration was successful.
            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so render form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request, 'account/register.html',
        context = {'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered})
        
def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password from login form.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # If valid, return user object
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                login(request, user)
                return redirect(reverse('oneWordStory:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided so user cannot log in.
            print(f"Invalid login details: {username}, {password}")
            return redirect(reverse('oneWordStory:login'))
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the blank dictionary object.
        return render(request, 'account/login.html')
    
    
# login_required() decorator ensures only those logged in can access the view.
@login_required
def user_logout(request):
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('oneWordStory:home'))
    

class LikeStoryView(View):
    #Works in tandem with ajax to update the number of likes when the like button is clicked
    @method_decorator(login_required)
    def get(self, request):
        story_name_slug = request.GET['story_slug']
        
        try:
            story = Story.objects.get(slug=story_name_slug)
        except Story.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        
        story.likes = story.likes + 1
        story.save()
        
        return HttpResponse(story.likes)