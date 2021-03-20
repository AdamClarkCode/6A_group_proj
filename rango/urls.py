from django.urls import path
from rango import views

app_name = 'rango'


urlpatterns = [
    path('', views.home, name='home'),
    path('add_story/', views.add_story, name='add_story'),
    path('register/', views.register, name='register'),

]
