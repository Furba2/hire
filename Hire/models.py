from django.db import models

# Create your models here.

class Service(models.Model):
    text = models.CharField()

    def __str__(self):
        return self.text

class Problem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    text = models.CharField()

    def __str__(self):
        return self.text