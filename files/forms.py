from dataclasses import fields
from django.forms import ModelForm
from .models import File, Shared
from django import forms
from users.models import Profile

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = [
            'uploaded_file'
        ]

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ShareForm(ModelForm):
    class Meta: 
        model = Shared    
        fields = [
            'files', 'share_with',
        ]
        widgets = { 
            'files': forms.CheckboxSelectMultiple(),
            'share_with': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(ShareForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        