# views.py

from django.shortcuts import render
from . database import insert_top_artists, insert_top_songs, insert_browse_all

def insert_data(request):
    # Call the functions to insert data into the database
    insert_top_artists()
    insert_top_songs()
    insert_browse_all()

    return render(request, 'insert_success.html')
