from django.db import models

# Create your models here.

class ReplicateData(models.Model):
    image_url = models.CharField(max_length=500,null=True,blank=True)
    name = models.CharField(max_length=100 ,null=True,blank=True)
    owner = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    run_count = models.CharField(max_length=30,null=True,blank=True)
    url = models.CharField(max_length=400,null=True,blank=True)
    key = models.IntegerField(null=False,default=1)
    
    