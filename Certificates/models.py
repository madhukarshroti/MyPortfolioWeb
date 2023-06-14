from django.db import models

# Create your models here.
class Certificate(models.Model):
    prject_id = models.AutoField
    
    image = models.ImageField(upload_to='Project/images', default="")
    Certificate_name = models.CharField(max_length=100)
    Certificate_tag = models.CharField(max_length=50)
    Certificate_date = models.CharField(max_length=20)