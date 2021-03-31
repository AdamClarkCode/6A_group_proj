from django.contrib import admin
from oneWordStory.models import Story, UserProfile

# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Story, StoryAdmin)