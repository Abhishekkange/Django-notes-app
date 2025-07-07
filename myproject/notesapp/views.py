from django.shortcuts import render,HttpResponse
from .models import ToDo

# Create your views here.
def createNote(request):
    #logic to create a new node
    return render(request,'createnote.html')

def showAllNotes(request):
    notes = ToDo.objects.all().order_by('-created_at')  # newest first
    #return notes html with Notes in DB
    return render(request,'allNotes.html',{"notes":notes})


def submitNote(request):
    if request.method == "POST":
        #get body data
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_at = request.POST.get('created_at')
        updated_at = request.POST.get('updated_at')

        #save to db
        todo = ToDo(title=title,description=description)
        todo.save()
        print("New to-do created...")
        return HttpResponse("Note created !!")
    
def getNotes(request):
    #get notes from db and then send it as html cards
    notes = ToDo.objects.all().order_by('-created_at')
    #loop through these notes

def updateNote(request):
    #check for POST request 
    if request.method == "POST":
        try:

            old_title = request.POST.get("old_title")
            new_title = request.POST.get("new_title")
            new_description = request.POST.get("new_description")
            #find obj using old title and update the title and description with new ones
            todo = ToDo.objects.get(title=old_title)
            todo.title = new_title
            todo.description = new_description
            print("Note Updated")
            return HttpResponse("Note Updated Successfully !")
        except:
            print("Note not found !")
            return HttpResponse("Note not found !")
        
    
