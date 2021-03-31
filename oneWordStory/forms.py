from django import forms
from oneWordStory.models import Story
from django.contrib.auth.models import User
from oneWordStory.models import UserProfile


class StoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
    help_text="Please enter the story name.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Story
        fields = ('name',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)