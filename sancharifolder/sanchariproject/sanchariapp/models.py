from django.db import models


# Create your models here.
class Placedetails(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name

class actors(models.Model):
    imag = models.ImageField(upload_to='pics')
    nam = models.CharField(max_length=250)
    descrip = models.TextField()

    def __str__(self):
        return self.nam

