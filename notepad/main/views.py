from django.shortcuts import render
from .models import Notes
from django.shortcuts import redirect
from string import ascii_lowercase as alph
from random import randint

# Create your views here.

def index(request):
	notes = Notes.objects.all()
	return render(request, "main/index.html", {'notes': notes})

def new(request):
	gen = ''
	for x in range(10):
		gen += alph[randint(0, len(alph) - 1)]
	print('New id ->', gen)
	return redirect(f'/{gen}/')

def note(request, ID):
	notes = Notes.objects.all()
	noteData = {'noteid': ID, 'title': 'Untitled', 'author': 'Unknown', 'text': '', 'change': 0}
	for note in notes:
		note = str(note).split('|')
		print(note)
		if note[0] == ID:
			noteData['title'] = note[1]
			noteData['author'] = note[2]
			noteData['text'] = note[3]
			noteData['change'] = 1
	return render(request, "main/note.html", noteData)