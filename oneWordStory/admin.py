from django.contrib import admin
from oneWordStory.models import Story, Word, UserProfile

# Register your models here.

admin.site.register(Story)
admin.site.register(UserProfile)
admin.site.register(Word)