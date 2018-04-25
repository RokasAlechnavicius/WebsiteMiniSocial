from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
import datetime

def validate_telephone(value):
    if len(str(value))>15:
        raise ValidationError('Telephone number must be less than 16 digits')

def validate_city(value):
    if len(value)>30:
        raise ValidationError("City value cannot be more than 30 characters")

def validate_description(value):
    if len(value)>200:
        raise ValidationError("Description is too long. Please reduce it to 200 characters or less")
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True,validators=[validate_description])
    city = models.CharField(blank=True,null=True,max_length=30,validators=[validate_city])
    phonenumber = models.IntegerField(blank=True,null=True,validators=[validate_telephone])

    def __str__(self):
        return self.user.username


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)


class ErrorLoggingManager(models.Manager):
    def create_error(self,error_text):
        error = self.create(error_text=error_text)
        return error


class ErrorLogging(models.Model):
    error_text = models.CharField(max_length=250)
    error_time = models.DateTimeField(default=datetime.datetime.now())
    objects = ErrorLoggingManager()

    def __str__(self):
        return self.error_text
