from django.db.models.signals import post_save #signals that get fired after a post is save 
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from .models import Profile 

@receiver(post_save, sender=User) #when a user is saved, send a signal received by a receiver which is a create profile function
#create profile function takes all  the arguments that signal passed to it 
#what the fuck 
def create_profile(sender, instance, created, **kwargs): 
    if created: 
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs): 
    instance.profile.save()