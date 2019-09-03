from django.contrib import admin
from .models import Blog, BlogCategory


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',  'created', 'status', )


admin.site.register(BlogCategory)
admin.site.register(Blog, BlogAdmin)