from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print('user logged in')
 
 
@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    print('user logged in failed')
 
 
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print('user logged out')