from django.urls import path
from . import views
from .views import profile_view, settings_view

urlpatterns = [
    #path('', views.index),
    path('', profile_view, name='main_profile'),
    path('profile', profile_view, name='profile'),
    path('settings', settings_view, name='settings')
]