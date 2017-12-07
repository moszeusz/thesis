from django.contrib import admin

from .models import UploadFile


class UploadFileAdmin(admin.ModelAdmin):
    # fields = ['file']
    search_fields = ('file',)
    list_per_page = 25
    list_display = ('file', 'as_photo',)
    ordering = ('-file',)  # sortuj od końca


admin.site.register(UploadFile, UploadFileAdmin)
