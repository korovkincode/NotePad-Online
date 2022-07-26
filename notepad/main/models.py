from django.db import models

# Create your models here.

class Notes(models.Model):
	noteid = models.CharField('NoteID', max_length = 10)
	title = models.CharField('Title', max_length = 30)
	author = models.CharField('Author', max_length = 30)
	text = models.TextField(help_text = "")
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return f'{self.noteid}|{self.title}|{self.author}|{self.text}'

	class Meta:
		verbose_name = 'Заметка'
		verbose_name_plural = 'Заметки'