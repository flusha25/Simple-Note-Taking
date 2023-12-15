from django.urls import path
from .views import *

urlpatterns = [
    path('',main_view,name =  'main_page'),
    path('add_note/', add_note , name = 'add_note'),
    path('delete_note/<int:title>', delete_note , name = 'delete_note'),
    path('details/<int:id>',note_details, name = 'note_details'),
    path('edit/<int:id>', edit_note, name = 'edit_note'),
]
