import matlab.engine
from django.http import HttpResponse, FileResponse
from django.views.generic import ListView, FormView, View
from mainpage.forms import UploadFileForm

from .models import UploadFile


class UploadFileListView(ListView):
    model = UploadFile


class UploadFileView(FormView):
    form_class = UploadFileForm
    template_name = 'mainpage/my_formview.html'
    # success_url = 'files/'
    success_url = 'download/'

    def form_valid(self, form):
        form.save()  # ModelForm posiada metodę save(), a form jest instancją ModelForm
        return super(UploadFileView, self).form_valid(form)
        # return HttpResponseRedirect(self.get_success_url())


class DownloadFileView(View):
    template_name = 'mainpage/downloadfile.html'

    @staticmethod
    def get(request):
        filename_path = '/home/moszeusz/django/simulator/media/' + UploadFile.objects.last().file.name

        eng = matlab.engine.start_matlab()
        eng.cd(r'/home/moszeusz/django/simulator/media', nargout=0)
        # eng.audio_proc(' ' + filename_path)
        eng.audio_proc(UploadFile.objects.last().file.name)

        content = FileResponse(open('/home/moszeusz/django/simulator/media/output2.mp3', 'rb'))
        response = HttpResponse(content, content_type="application/mp3")
        # response['Content-Length'] = os.path.getsize(attachment)
        response[
            'Content-Disposition'] = "attachment; filename=%s" % 'processed_audio.mp3'  # nazwa, pod jaka zostanie zapisany plik
        return response
