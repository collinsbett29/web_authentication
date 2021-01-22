from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField


class Profile(models.Model):
    ADMIN = 1
    USER = 2
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User')
    )
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

class UserPicture(models.Model):
        user = models.OneToOneField(User, on_delete = models.CASCADE)
        picture = models.ImageField(upload_to='...')
        
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()