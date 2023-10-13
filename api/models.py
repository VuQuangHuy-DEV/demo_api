from django.db import models

# Create your models here.
class Book(models.Model):
    title             = models.CharField(max_length=150)
    author            = models.CharField(max_length=100)
    publiccation_date = models.DateField()
    description       = models.CharField(max_length=1000)
    price             = models.FloatField
    languge           = models.CharField(max_length=20)

    def __str__(self):
        return self.name



