from django import forms
from django.contrib.auth.models import User
from oneWordStory.models import Story, UserProfile, Word
from django.core.exceptions import ValidationError
from django.core import validators

class StoryForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the story name.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Story
        fields = ('title',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class WordForm(forms.ModelForm):
    content = forms.CharField(max_length=128, help_text="What comes next?",validators=[validators.validate_slug])
    
    class Meta:
        model = Word
        fields = ('content',)
