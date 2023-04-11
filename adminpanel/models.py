from django.db import models

# Create your models here.
class Contact(models.Model):
    number1=models.CharField(max_length=40,null=True,blank=True)
    number2=models.CharField(max_length=40,null=True,blank=True)
    email=models.EmailField()
    facebook=models.CharField(max_length=200,null=True,blank=True)
    telegram=models.CharField(max_length=200,null=True,blank=True)
    instagram=models.CharField(max_length=200,null=True,blank=True)
    linkedin=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return 'contact'

class Search_Book(models.Model):
    text=models.TextField()
    count_search=models.PositiveIntegerField(null=True,blank=True,default=1)

    def __str__(self):
        return self.text
class Search_File(models.Model):
    text=models.TextField()
    count_search=models.PositiveIntegerField(null=True,blank=True,default=1)

    def __str__(self):
        return self.text
