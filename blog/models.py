from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from votes.managers import VotableManager

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	votes = VotableManager()
	chismes_de = models.CharField(
		max_length=20,
		choices=(('Alumno','Alumno'), ('Profesor', 'Profesor'), ('Otros', 'Otros')),
		default='Alumno',
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



		
