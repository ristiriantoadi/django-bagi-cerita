from django.contrib import admin
from .models import Story,Tag,Comment

# Register your models here.
admin.site.register(Story)
admin.site.register(Tag)
admin.site.register(Comment)