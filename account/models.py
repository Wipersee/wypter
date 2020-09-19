from django.db import models
from django.conf import settings
from PIL import Image


class Profile(models.Model):
  """
  This class is extension of default django user model
  We rewrite the save method to optimize the photo
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

  def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)
    if self.photo:
      image = Image.open(self.photo.path)
      image.save(self.photo.path, quality=20, optimize=True)
