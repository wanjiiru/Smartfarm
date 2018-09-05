from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.db.models import PointField
from django.db.models.signals import post_save
from django.contrib.gis.gdal import DataSource
from django.dispatch import receiver
from smartfarm.settings import BASE_DIR

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
    locality = models.ForeignKey('County')

    def save(self,*args,**kwargs):
        commit = kwargs.get('commit')
        if commit is None or commit == True:
            self.locality = next(county for county in County.objects.all() if county.geom.contains(self.location))
        super().save(*args,**kwargs)


class Diseases(models.Model):
    name = models.TextField()
    Image = models.ImageField(upload_to='gross')
    control = models.TextField()
    symptoms = models.TextField()

    def __str__(self):
        return self.name


class County(models.Model):
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    county3_field = models.FloatField()
    county3_id = models.FloatField()
    county = models.CharField(max_length=20)
    shape_leng = models.FloatField()
    shape_area = geomodels.FloatField()
    geom = geomodels.MultiPolygonField(srid=4326)

    def __str__(self):
        return f"{self.county}"

    class Meta:
        verbose_name_plural = 'County'

