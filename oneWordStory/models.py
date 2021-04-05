from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    likes = models.IntegerField(default=0)
    
    author = models.ForeignKey(
        'UserProfile', on_delete=models.CASCADE
    )
    class Meta:
        verbose_name_plural = 'Stories'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
        
class Word(models.Model):
    content = models.CharField(max_length=128)
    userProfile = models.ForeignKey(
        'UserProfile', on_delete=models.CASCADE
    )
    story = models.ForeignKey(
        'Story', on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.content
        
class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional attributes to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    slug = models.SlugField(unique=True)
     
    contributions = models.ManyToManyField('Story')
     
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username

