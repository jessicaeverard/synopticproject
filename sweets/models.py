from django.db import models

class Sweets(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    price = models.FloatField()
    image = models.ImageField(upload_to='sweet/images/')

    def __str__(self):
        return self.name