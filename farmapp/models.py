from django.contrib.gis.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
# from django.db import models
=======
from django.contrib.gis.db.models import PointField
>>>>>>> 919dc27da3bcecfaf68a09ab4e834daba277fb90
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

