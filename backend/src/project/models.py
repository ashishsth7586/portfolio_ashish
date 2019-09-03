from django.db import models


class ProjectCategory(models.Model):
    category = models.CharField(max_length=50, default="Project category")

    class Meta:
        ordering = ['-category']
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'

    def __str__(self):
        return self.category


class Project(models.Model):
    page_heading = models.CharField(max_length=10, default="Project")
    title = models.CharField(max_length=150, default="Project Title")
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='images/project/thumbnail', null=True)

    def __str__(self):
        return self.title
