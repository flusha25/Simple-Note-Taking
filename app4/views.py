

from django.shortcuts import render, redirect
from .models import Note
from django.shortcuts import get_object_or_404

def main_view(request): 
    notes = Note.objects.all()
    return render(request , 'main_page.html', {'notes':notes})

def add_note(request):
    
    if request.method == 'POST':
        new_note = Note(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            date_created = request.POST.get('date_created'),
        )
        new_note.save()
        return redirect('add_note')
    return render(request, 'add_note.html')
def note_details(request, id):
    DETAIL = Note.objects.get(id=id)
    return render(request , 'note_detail.html', {'note':DETAIL})

    
def delete_note(request,title):
    try:
        delete = Note.objects.get(id=title)
        delete.delete()
        return render(request, 'deleted.html')
    except  Note.DoesNotExist:
        return render(request, 'main_page.html')
    
def edit_note(request, id):
    note = Note.objects.get(id=id)

    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')

        note.save()
        return redirect('note_details', id=id)
    
    return render(request, 'edit_note.html', {'note': note})    
    