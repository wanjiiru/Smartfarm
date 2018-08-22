from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Profile
from .models import Image
from .brain.brain import recognise
from .forms import ImageForm
from base64 import b64encode
from io import BytesIO

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html', {})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile = ProfileForm(instance=request.user.profile)

    return render(request, 'index.html',{"user_form":user_form,"profile_form":profile_form})

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
