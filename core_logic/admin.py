from django.contrib import admin
from . import models

admin.site.register(models.Wallet)
admin.site.register(models.Category)
admin.site.register(models.Extend)
admin.site.register(models.Income)
admin.site.register(models.MonthlyExtend)
