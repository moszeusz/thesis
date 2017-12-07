from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, FormView
from mainpage.forms import UploadFileForm

from .models import UploadFile


class UploadFileListView(ListView):
    model = UploadFile


class UploadFileView(FormView):
    form_class = UploadFileForm
    template_name = 'mainpage/my_formview.html'
    success_url = 'download/'

    def form_valid(self, form):
        form.save()  # ModelForm posiada metodę save(), a form jest instancją ModelForm
        # return super(UploadFileView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

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
