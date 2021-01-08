from django import forms
from .models import Shorten
class ShortenForm(forms.ModelForm):
    class Meta:
        model = Shorten
        exclude = ("link",)