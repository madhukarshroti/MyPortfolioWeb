from django.db import models

# Create your models here.
class ServicesSec(models.Model):
    prject_id = models.AutoField
    
    icon = models.CharField(max_length=50)
    Service = models.CharField(max_length=100)
    ServiceDetail = models.TextField()
    
    
    