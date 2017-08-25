from django import forms
from .models import Chat
from .models import Post
from .models import Document
from .models import Comment

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('titulo', 'texto', 'chismes_de')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('titulo', 'texto', 'chismes_de', 'archivo')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('texto',)