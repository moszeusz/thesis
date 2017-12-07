from django import forms
from mainpage.models import UploadFile


class UploadFileForm(forms.ModelForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = UploadFile
        fields = ('file',)

# TODO w dokumentacji pod "customizing validation"
    # def clean_file(self):
    #     data = self.cleaned_data['file']
    #     if 'mp3' not in data:
    #         raise forms.ValidationError("To musi być plik z rozszerzeniem .mp3")
    #     return data
