from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("INSIDE CREATE_PROFILE")#negative
    if created:
        print("INSIDE CREATED_PROFILE")#negative
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): #kwargs= accepts any additional keywords
        instance.profile.save()

@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs): #kwargs= accepts any additional keywords
        instance.profile.delete()