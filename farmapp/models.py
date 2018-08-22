from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    email = models.EmailField(max_length=254,null=True)

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
    counties = (
        ('Baringo County', 'Baringo County'),
        ('Bomet County', 'Bomet County'),
        ('Bungoma County', 'Bungoma County'),
        ('Busia County', 'Busia County'),
        ('Elgeyo Marakwet County', 'Elgeyo Marakwet County'),
        ('Embu County', 'Embu County'),
        ('Garissa County', 'Garissa County'),
        ('Homa Bay County', 'Homa Bay County'),
        ('Isiolo County', 'Isiolo County'),
        ('Kajiado County', 'Kajiado County'),
        ('Kakamega County', 'Kakamega County'),
        ('Kericho County', 'Kericho County'),
        ('Kiambu County', 'Kiambu County'),
        ('Kilifi County', 'Kilifi County'),
        ('Kirinyaga County', 'Kirinyaga County'),
        ('Kisii County', 'Kisii County'),
        ('Kisumu County', 'Kisumu County'),
        ('Kitui County', 'Kitui County'),
        ('Kwale County', 'Kwale County'),
        ('Laikipia County', 'Laikipia County'),
        ('Lamu County', 'Lamu County'),
        ('Machakos County', 'Machakos County'),
        ('Makueni County', 'Makueni County'),
        ('Mandera County', 'Mandera County'),
        ('Meru County', 'Meru County'),
        ('Migori County', 'Migori County'),
        ('Marsabit County', 'Marsabit County'),
        ('Mombasa County', 'Mombasa County'),
        ('Muranga County', 'Muranga County'),
        ('Nairobi County', 'Nairobi County'),
        ('Nakuru County', 'Nakuru County'),
        ('Nandi County', 'Nandi County'),
        ('Narok County', 'Narok County'),
        ('Nyamira County', 'Nyamira County'),
        ('Nyandarua County', 'Nyandarua County'),
        ('Nyeri County', 'Nyeri County'),
        ('Samburu County', 'Samburu County'),
        ('Siaya County', 'Siaya County'),
        ('Taita Taveta County', 'Taita Taveta County'),
        ('Tana River County', 'Tana River County'),
        ('Tharaka Nithi County', 'Tharaka Nithi County'),
        ('Trans Nzoia County', 'Trans Nzoia County'),
        ('Turkana County', 'Turkana County'),
        ('Uasin Gishu County', 'Uasin Gishu County'),
        ('Vihiga County', 'Vihiga County'),
        ('Wajir County', 'Wajir County'),
        ('West Pokot County', 'West Pokot County'),
    )
    location = models.CharField(max_length=255, choices=counties)
    pic = models.ImageField()

    def __str__(self):
        return self.pic

        
