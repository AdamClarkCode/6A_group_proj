from django.urls import path
from oneWordStory import views

app_name = 'oneWordStory'


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('add_story/', views.add_story, name='add_story'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('<slug:story_name_slug>/', views.show_story, name='show_story'),
    path('<slug:user_name_slug>/', views.show_profile, name='show_profile'),

]
