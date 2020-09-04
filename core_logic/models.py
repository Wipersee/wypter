from django.db import models
from account.models import Profile


class Wallet(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    choices = (
        ('UAH', 'ukraine hryvna'),
        ('USD', 'Dollars'),
        ('RUB', 'russian rubles'),
        ('EUR', 'euros')
    )
    courency = models.CharField(
        max_length=3,
        choices=choices,
        default='UAH'
    )
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return f'This is the wallet of {self.user.user}'


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Extend(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    comment = models.CharField(max_length=256)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return self.price


class Income(models.Model):
    price = models.PositiveIntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return self.price