from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=20)
	texto = models.TextField()
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

		
class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=50)

    def __unicode__(self):
        return self.message



class Document(models.Model):
    titulo = models.CharField(max_length=20)
    texto = models.TextField(blank=True)
    chismes_de = models.CharField(
		max_length=20,
		choices=(('Alumno','Alumno'), ('Profesor', 'Profesor'), ('Otros', 'Otros')),
		default='Alumno',
	)
    archivo = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User')
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.texto


def approved_comments(self):
    return self.comments.filter(approved_comment=True)