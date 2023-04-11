from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
from filestore import settings


class User_coin(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    coins=models.PositiveIntegerField(null=True,blank=True,default=0)
    created_data=models.DateField(auto_now_add=True)



    def __str__(self):
        return   f"{self.user.username}     t {self.user.email}   {self.coins}"

    def email(self):
        return self.user.email

    def username(self):
        return self.user.username