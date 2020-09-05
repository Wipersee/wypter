from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    """This class is extension of default django user
    model"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
        return f'This account of {self.user.username}'
