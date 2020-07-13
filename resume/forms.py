from django import forms
from resume.models import Resume


class FileForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["name", "filepath"]
