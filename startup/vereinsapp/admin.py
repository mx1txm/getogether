from django.contrib import admin
from .models import Post, Snippet, Author

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Snippet)
