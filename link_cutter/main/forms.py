from django import forms
from .models import Url

class LinkCutterForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['full_url']
        widgets = {
            'full_url': forms.URLInput(attrs={'size': 100})
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'




















