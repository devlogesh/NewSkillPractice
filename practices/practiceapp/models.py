from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Userprofile(models.Model):
   
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,db_column='user_id',null=True,blank=True)
    email = models.CharField(max_length=50,unique=True,null=True,blank=True)
    mobile = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=50,null=True,blank=True)
    
    class Meta:
        db_table = 'userprofile'
        ordering = ['-id']

class AccessToken(models.Model):
    key = models.CharField(max_length=255)
    user_id = models.ForeignKey(User,on_delete=models.PROTECT,db_column='user_id')
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'accesstoken'
        ordering = ['-id']