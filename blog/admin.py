from django.contrib import admin
from .models import Post
from .models import Chat
from .models import Document
from .models import Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Chat)
admin.site.register(Document)
