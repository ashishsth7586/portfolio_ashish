from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class BlogCategory(models.Model):
    category = models.CharField(max_length=50, default="blog category")

    class Meta:
        ordering = ['-category']
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.category


class Blog(models.Model):
    title = models.CharField(max_length=100, default="Blog Title")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(default='', blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='images/blog/thumbnail', null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    content_excerpt = models.CharField(max_length=180, default="max 180 characters", blank=True)
    content = RichTextUploadingField(null=True,
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/vendor/ckeditor_plugins/youtube/',
                                         'plugin.js',
                                     )],
                                     )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
