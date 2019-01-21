from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 50)
    phone = models.IntegerField()
    text = models.TextField(max_length = 144)
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name