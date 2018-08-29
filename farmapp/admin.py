from django.contrib import admin
from .models import Image, Diseases, detect

# Register your models here.
admin.site.register(Image)
admin.site.register(Diseases)
admin.site.register(detect)
