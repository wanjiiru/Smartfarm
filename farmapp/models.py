from django.contrib.gis.db import models
from django.contrib.auth.models import User
from requests.utils import quote
import requests
from django.contrib.gis.db.models import PointField
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True, related_name="profile")
    email = models.EmailField(max_length=254,null=True)
    bio = models.TextField(max_length=500,blank=True)
    location = models.CharField(max_length=30,blank=True)

    def __str__(cls):
        return cls.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Image(models.Model):
    location =models.PointField()
    pic = models.ImageField(upload_to='gross')







class Diseases(models.Model):
    name = models.TextField()
    Image = models.ImageField(upload_to='gross')
    control = models.TextField()
    symptoms = models.TextField()

    def __str__(self):
        return self.name


class detect(models.Model):
    location = models.TextField()
    disease = models.ForeignKey(Diseases)
    locality = models.TextField()

    def save(self,*args,**kwargs):
        # get lat,lon from liz
        url = 'http://www.datasciencetoolkit.org/coordinates2politics/' + quote(f'[["{lat}","{lon}"]]')
        respo = requests.get(url)
        zones = respo[0]['politics']
        country, county = [x['name'] for x in zones]
        self.locality = county
        super().save(*args,**kwargs)
