
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image
from .brain.brain import recognise
from .forms import ImageForm
from base64 import b64encode
from io import BytesIO

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # add=form.save(commit=False)
            # add.owner = current_user
            image = next(request.FILES.values()).read()
            results = recognise(BytesIO(image))

            buffer = b64encode(image)

            # add.save()
            return render(request, 'results.html', locals())
    else:
        form = ImageForm()


    return render(request,'image.html',locals())

def how_it_works(request):

    return render(request,'how.html', locals())
