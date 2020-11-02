from django import forms
from .models import MyFiles

class UploadDocumentForm(forms.ModelForm):
    # file = forms.FileField()
    # # image = forms.ImageField()

    class Meta:
        model = MyFiles
        fields = ['my_file']