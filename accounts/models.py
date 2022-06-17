from this import s
import django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Profile)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()