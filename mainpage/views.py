import os
from wsgiref.util import FileWrapper
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView, View, TemplateView
from mainpage.forms import UploadFileForm

from .models import UploadFile


class UploadFileListView(ListView):
    model = UploadFile


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            return destination.write(chunk)


class UploadFileView(FormView):
    form_class = UploadFileForm
    template_name = 'mainpage/my_formview.html'
    # success_url = 'files/'
    success_url = 'download/'

    def form_valid(self, form):
        form.save()  # ModelForm posiada metodę save(), a form jest instancją ModelForm
        return super(UploadFileView, self).form_valid(form)
        # return HttpResponseRedirect(self.get_success_url())


# class UploadFileView(FormView):
#     template_name = 'mainpage/my_formview.html'
#     form_class = MainForm
#     success_url = 'files/'
#
#     def form_valid(self, form):
#         upload_file = UploadFile(
#             file=self.get_form_kwargs().get('files')['file'])
#         upload_file.save()
#
#         return HttpResponseRedirect(self.get_success_url())


class DownloadFileView(View):
    # template_name = 'mainpage/downloadfile.html'

    @staticmethod
    def get(request):
        filename = '/home/moszeusz/django/simulator/media/sample.mp3'
        # attachment = FileWrapper(open(path.abspath(filename), 'rb'))
        # attachment = handle_uploaded_file(request.FILES['/home/moszeusz/django/simulator/media/sample.mp3'])

        # attachment = request.body
        # response = HttpResponse(attachment, content_type="application/mp3")
        # response['Content-Length'] = os.path.getsize(attachment)
        # response[
        #     'Content-Disposition'] = "attachment; filename=%s" % "Visez.mp3"  # nazwa, pod jaką zostanie zapisany plik
        return HttpResponse(request.read())

# def download_pdf(request):
# filename = 'whatever_in_absolute_path__or_not.pdf'
# content = FileWrapper(filename)
# response = HttpResponse(content, content_type='application/pdf')
# response['Content-Length'] = os.path.getsize(filename)
# response['Content-Disposition'] = 'attachment; filename=%s' % 'whatever_name_will_appear_in_download.pdf'
# return response

# class ExportData(View):
#     @staticmethod
#     def get(request, export_format):
#         if export_format == 'json':
#             attachment = export_json()
#             response = HttpResponse(attachment, content_type="application/json")
#             response['Content-Disposition'] = "attachment; filename=TLEMS_export.json"
#         else:
#             attachment = export_xls()
#             response = HttpResponse(attachment,
#                                     content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
#             response['Content-Disposition'] = "attachment; filename=TLEMS_export.xlsx"
#         return response
