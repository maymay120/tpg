from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class history(models.Model):
    user = models.ForeignKey(User, related_name='history', on_delete=models.CASCADE)
    buy_sold = models.BooleanField()
    status = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
    

class profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    file = models.FileField(blank=True, null=True, upload_to='webimg/')
    back = models.FileField(blank=True, null=True, upload_to='webimg/')
    file2 = models.FileField(blank=True, null=True, upload_to='webimg/')
    verified = models.BooleanField(default=False)
    email_verify = models.BooleanField(default=False)
    num = models.CharField(max_length=100, default=0)
    num2 = models.CharField(max_length=200, default=0)
    address = models.TextField(blank=True, null=True)
    principle_value = models.IntegerField(default=0)
    dob = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=400, blank=True, null=True)
    postal = models.CharField(max_length=500, blank=True, null=True)
    credit = models.IntegerField(default=0)
    refer_num = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

class principal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    principal = models.IntegerField()
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

class accured(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=20000, blank=True, null=True, default=0)
    date = models.DateTimeField(default=0, null=True, blank=True)
    new_date = models.DateTimeField(default=0, null=True, blank=-True)

    def __str__(self):
        return str(self.user)

class otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, blank=True, null=True, default=0)