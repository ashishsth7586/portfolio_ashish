from django.contrib import admin
from .models import Project, ProjectCategory


admin.site.register(ProjectCategory)
admin.site.register(Project)