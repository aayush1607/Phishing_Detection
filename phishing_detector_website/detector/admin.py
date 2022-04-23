from django.contrib import admin

from .models import Website,WebsiteAdmin
# Register your models here.

admin.site.register(Website,WebsiteAdmin)