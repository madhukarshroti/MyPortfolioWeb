from django.db import models

class Skills(models.Model):
    skill_name = models.CharField(max_length=60)
    skill_value = models.IntegerField()
# Create your models here.
