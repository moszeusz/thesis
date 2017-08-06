from django.contrib import admin

from mainpage.models import UploadFile


class UploadFileAdmin(admin.ModelAdmin):
    fields = ["file"]
    # list_display = ('file')


admin.site.register(UploadFile, UploadFileAdmin)
