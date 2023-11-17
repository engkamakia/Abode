from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import Realtor
from django.contrib.auth.models import Group

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
       group = Group.objects.get(name = "realtor")
       instance.groups.add(group)
       Realtor.objects.create(user=instance,email = instance.email)
        
#@receiver(post_save, sender = User)       
#def update_profile(sender, instance, created,**kwargs):
    #if created == False:
        #instance.realtor.save()
        #print("Profile updated!")
        