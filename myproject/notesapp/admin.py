from django.contrib import admin

# Register your models here.
from .models import ToDo
from .models import ToDoHistory

admin.site.register(ToDo)
admin.site.register(ToDoHistory)
