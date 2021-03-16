from django import forms
from rango.models import Story

class StoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
    help_text="Please enter the story name.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Story
        fields = ('name',)
