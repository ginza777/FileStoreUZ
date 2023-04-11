from django.db import models
import datetime
# Create your models here.
from django.urls import reverse
from django.template.defaultfilters import slugify
import os

class Books(models.Model):
    name=models.CharField(max_length=300,null=True,blank=True)
    title=models.TextField(null=True,blank=True,default="filestore.uz")
    img=models.ImageField(upload_to='books/img',default='books/img/img.jpg')
    file=models.FileField(upload_to='books/books',default='books/file/file.pdf')
    coin=models.PositiveIntegerField(null=True,blank=True,default=0)
    download_count=models.PositiveIntegerField(null=True,blank=True,default=0)
    view=models.PositiveIntegerField(null=True,blank=True,default=0)
    created_data=models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True,blank=True, unique=True)
    tag = models.TextField(null=True, blank=True)
    star=models.PositiveIntegerField(null=True,blank=True,default=3)
    #
    # def file_size(self):
    #     return os.path.basename(self.file.size)
    #
    #


    def save(self, *args, **kwargs):  # new
        if not self.name:
            self.name=os.path.basename(self.file.name)
        if not self.slug:
            self.slug = slugify(f"{os.path.basename(self.file.name)}+{self.name}")
        if not self.tag:
            self.tag=f"""{os.path.basename(self.file.name)}+{self.title}"""
        if self.tag:
            self.tag=self.tag+f"""/{os.path.basename(self.file.name)}/{self.title}"""





        return super().save(*args, **kwargs)





