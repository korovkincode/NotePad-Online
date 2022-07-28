from django.forms import ModelForm, TextInput, Textarea
from .models import Notes

class NoteForm(ModelForm):
	class Meta:
		model = Notes
		fields = ['noteid', 'title', 'author', 'text']

		labels = {'text': ''}
		widgets = {
		'noteid': TextInput(attrs = {'readonly':'readonly', 'size': 8, 'style': 'background-color: inherit; border: 0; color: inherit; font-size: 30px; outline: none; text-align: center;', 'initial': 'Untitled'}),
		'title': TextInput(attrs = {'size': 8, 'style': 'background-color: inherit; border: 0; color: inherit; font-size: 30px; outline: none; text-align: center;', 'initial': 'Untitled'}),
		'author': TextInput(attrs = {'size': 8, 'style': 'background-color: inherit; border: 0; color: inherit; font-size: 30px; outline: none; text-align: center;', 'initial': 'Untitled'}),
		'text': Textarea(attrs = {'class': 'editor'})
		}
	def set_step(self, step):
	    data = self.data.copy()
	    data['noteid'] = step
	    self.data = data