from django.db import models

# Create your models here.

class Temp(models.Model):
    env_temp = models.FloatField()
    obj_temp = models.FloatField()
    distance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)