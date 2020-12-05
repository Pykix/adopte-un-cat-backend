from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from users.models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )
