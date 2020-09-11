from django.db import models
from account.models import Profile


class Wallet(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    choices = (
        ('UAH', 'Ukraine hryvna'),
        ('USD', 'Dollars'),
        ('RUB', 'Russian rubles'),
        ('EUR', 'Euros')
    )
    courency = models.CharField(
        max_length=3,
        choices=choices,
        default='UAH'
    )
    balance = models.DecimalField(max_digits=20,
                                  decimal_places=2,
                                  default=0.00)

    def __str__(self):
        return f'This is the wallet of {self.user.user}'


class Category(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name


class Extend(models.Model):
    category = models.ForeignKey(
        Category, related_name='extends', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    comment = models.CharField(max_length=256)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date']
        

    def __str__(self):
        return f"{self.wallet.user.user.username} {self.category} {self.price}"


class Income(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.wallet.user.user.username} {self.price}"
