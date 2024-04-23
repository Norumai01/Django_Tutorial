from django.contrib import admin
from .models import Post

# Register your models here.
# Allow admin to view the Post section.
admin.site.register(Post)