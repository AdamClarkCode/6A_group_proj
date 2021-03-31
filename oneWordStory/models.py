from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    url = models.URLField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Story, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
        
class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    # Additional attributes to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    slug = models.SlugField(unique=True)
     
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Story, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username

