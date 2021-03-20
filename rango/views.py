from django.shortcuts import render
from django.http import HttpResponse
from rango.forms import StoryForm
from django.shortcuts import redirect
from rango.forms import UserForm, UserProfileForm


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