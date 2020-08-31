from django.db import models
from account.models import Profile

class Wallet(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    costs = models.IntegerField()
    income = models.IntegerField()

class Name_costs(models.Model):
    product = models.PositiveIntegerField(blank=True)
    technology = models.PositiveIntegerField(blank=True)
    play = models.PositiveIntegerField(blank=True)
    study = models.PositiveIntegerField(blank=True)
    health = models.PositiveIntegerField(blank=True)

class Costs(models.Model):
    cost = models.ForeignKey(Wallet, related_name='spending', on_delete=models.CASCADE)
    name_cost = models.ManyToManyField(Name_costs)

