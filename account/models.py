from django.db import models
from django.conf import settings


class Profile(models.Model):
    """
    This class is extension of default django user model
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    money_limit = models.DecimalField(max_digits=20,
                                      decimal_places=2,
                                      default=0.00)

    def __str__(self):
        return f'This account of {self.user.username}'
