# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('top_artists/', views.insert_top_artists, name='top_artists'),
    path('top_songs/', views.insert_top_songs, name='top_songs'),
    
     path('browse_all/', views.insert_browse_all, name='browse_all'),
    
]
