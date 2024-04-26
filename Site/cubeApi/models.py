from django.db import models

class Settings(models.Model):
    cube_power = models.BooleanField()
    light = models.BooleanField()
    heart = models.BooleanField()
    gender = models.BooleanField()
    sadness = models.BooleanField()
    wifi = models.BooleanField()
    temperature = models.BooleanField()
    water = models.BooleanField()
    tv = models.BooleanField()
    weather = models.BooleanField()

    def __str__(self):
        return self.cube_power