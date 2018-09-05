from django import forms
from .models import Image
from django.contrib.gis.db.models import PointField


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('location', 'locality')