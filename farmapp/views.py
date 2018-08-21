
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image
from .forms import ImageForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.owner = current_user
            add.save()
            return redirect('index')
    else:
        form = ImageForm()


    return render(request,'image.html',locals())

def how_it_works(request):


    return render(request,'how.html', locals())
