from django.contrib import admin

from .models import MyFiles

@admin.register(MyFiles)
class MyFilesAdmin(admin.ModelAdmin):
    pass
