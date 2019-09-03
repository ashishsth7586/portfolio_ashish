from django.contrib import admin
from .models import Landing, About, SocialMedia, Testimonial, Service, Quote
from django.contrib.auth.models import Group


admin.site.site_header = "Portfolio - Ashish Shrestha"
admin.site.site_title = "Dashboard | Portfolio | Ashish Shrestha"


class LandingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'introduction', )


admin.site.register(Landing, LandingAdmin)
admin.site.register(About)
admin.site.register(SocialMedia)
admin.site.register(Quote)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.unregister(Group)