from django.db import models

# Create your models here.
class ProjectShow(models.Model):
    prject_id = models.AutoField
    
    technology = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Project/images', default="")
    Feature1 = models.CharField(max_length=50, blank=True)
    Feature2 = models.CharField(max_length=50, blank=True)
    Feature3 = models.CharField(max_length=50, blank=True)
    Feature4 = models.CharField(max_length=50, blank=True)
    Feature5 = models.CharField(max_length=50, blank=True)
    ProjectTime = models.CharField(max_length=10)
    project_name = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    desc = models.TextField()
    desc2 = models.TextField(blank=True)
    
    def __str__(self):
        return self.project_name
    
    