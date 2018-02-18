from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.safestring import mark_safe


class UploadFile(models.Model):
    # file = models.FileField(verbose_name=_("file"), upload_to='%d %b %Y/%H:%M')
    file = models.FileField(verbose_name=_("plik"),)  # "_()" sluzy do tlumaczenia tekstu

    def __str__(self):
        return self.file

    def as_photo(self):
        if self.file.url:
            return mark_safe(u'<img src="%s" width="150" height="auto" />' % self.file.url)
        else:
            pass
    as_photo.short_description = 'image'

    class Meta:
        verbose_name = _('plik')
        verbose_name_plural = _('pliki')
