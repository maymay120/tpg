from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.history)
admin.site.register(models.profile)
admin.site.register(models.principal)
admin.site.register(models.accured)
admin.site.register(models.otp)