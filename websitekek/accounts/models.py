from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=200,default='')
    city = models.CharField(default='',max_length=30)
    phonenumber = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#
# post_save.connect(create_profile,sender=User)
