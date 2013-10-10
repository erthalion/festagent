from django.db import models

class FestManager(models.Manager):
    pass

class Fest(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    start_date = models.DateTimeField()

    objects = FestManager()
