from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	chismes_de = models.CharField(
		max_length=1,
		choices=(('A','Alumno'), ('P', 'Profesor'), ('O', 'Otros')),
		default='A',
	)
	created_date = models.DateTimeField(
		default=timezone.now)	
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo
		

