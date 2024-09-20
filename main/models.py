from django.db import models


# Create your models here.

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.JSONField()

    def __str__(self):
        return str(self.data)


class MetalStuff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    data = models.JSONField()

    def __str__(self):
        return str(self.data)


class Currency(models.Model):
    data = models.JSONField()

    def __str__(self):
        return str(self.data)
