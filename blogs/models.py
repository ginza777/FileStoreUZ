from django.db import models
import datetime
# Create your models here.
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True,default="filestore-blogs")
    description=models.TextField(null=True,blank=True,default="filestore-blogs-description")
    img=models.ImageField(null=True,blank=True,upload_to='blogs/img')
    view=models.PositiveIntegerField(null=True,blank=True,default=0)
    created_data=models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True,blank=True, unique=True)
    tag = models.TextField(null=True, blank=True)
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.tag:
            self.tag=f"""{self.description}+{self.title}"""



        return super().save(*args, **kwargs)



    def __str__(self):
        return self.title