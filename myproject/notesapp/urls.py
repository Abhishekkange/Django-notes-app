from django.contrib import admin
from django.urls import path
from .views import createNote,submitNote,showAllNotes



urlpatterns = [
    path('create-note',createNote, name='create-note'),
    path('submit-note',submitNote,name='submit-note'),
    path('allNotes',showAllNotes,name='allNotes')
]

