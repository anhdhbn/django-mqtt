from django.db import models

# Create your models here.

class MqttTest(models.Model):
    # id = models.CharField(max_length=200, unique=True, primary_key=True)
    env_temp = models.FloatField()
    obj_tmp = models.FloatField()
    distance = models.FloatField()

    def __str__(self):
        return f"Env temp: {self.env_temp}, Obj temp: {self.env_temp}, Distance: {self.distance}"