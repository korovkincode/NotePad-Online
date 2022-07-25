from django.db import models

# Create your models here.

class Notes(models.Model):
	noteid = models.CharField('NoteID', max_length = 10)
	title = models.CharField('Название', max_length = 30)
	author = models.CharField('Автор', max_length = 30)
	text = models.TextField('Статья')
	date = models.DateTimeField(null = True)

	def __str__(self):
		return f'{self.noteid}|{self.title}|{self.author}|{self.text}'

	class Meta:
		verbose_name = 'Заметка'
		verbose_name_plural = 'Заметки'