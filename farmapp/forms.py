from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
<<<<<<< HEAD
        exclude =['posted']




=======
        exclude =['owner', 'posted']
>>>>>>> 15d4059dc6d5eb49bb9ef5624aab89147b96173a
