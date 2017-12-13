from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from mainpage.views import UploadFileListView, UploadFileView, DownloadFileView

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'simulator.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = [
    # Examples:
    # url(r'^$', 'simulator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^files/$', UploadFileListView.as_view(), name='uploadfile-list'),
    url(r'^download/$', DownloadFileView.as_view(), name='downloadfile'),
    url(r'$', UploadFileView.as_view()),  # gdy dodany, brak podglądu plików statycznych w panelu admina
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
