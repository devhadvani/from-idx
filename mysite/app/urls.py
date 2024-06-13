
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
path('about/', views.about, name='about'),
    path('create_story/', views.create_story, name='create_story'),
    path('view_story/', views.view_story, name='view_story'),
    path('delete_story/<int:story_id>/', views.delete_story, name='delete_story'),
    path('login/', views.user_login, name='login'),
]
