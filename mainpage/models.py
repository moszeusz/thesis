from django.db import models
from django.utils.safestring import mark_safe


class UploadFile(models.Model):
    file = models.FileField(upload_to='%d %b %Y/%H:%M')
    # topic = models.ForeignKey('Topic', null=True)

    def __str__(self):
        return self.file.name  # + 'modified'

    def as_photo(self):
        return mark_safe(u'<img src="%s" width="150" height="150" />' % self.file.url)
    as_photo.short_description = 'Image'
