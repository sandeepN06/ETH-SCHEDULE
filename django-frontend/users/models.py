from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=50, blank=True) 
    last_name = models.CharField(max_length=50, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

    gender = models.CharField(max_length=30, blank=True)
    website_link = models.CharField(max_length=30, blank=True)
    social_media_link = models.CharField(max_length=30, blank=True)

    email = models.EmailField(max_length=120, blank=True)
    photo = models.ImageField(upload_to = "images/",blank = True)
    create_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.first_name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    # if created:
    #     Profile.objects.create(user=instance)
    # instance.profile.save()

    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
