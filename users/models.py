from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = INTERESTED_GENDER = (
    ('F', 'Femelle'),
    ('M', 'Male'),
)


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    interested_gender = models.CharField(max_length=1, choices=INTERESTED_GENDER)
    color = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)
    hobby = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return "{}".format(self.user.username)
