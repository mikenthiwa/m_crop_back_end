from django.db import models


# Create your models here.
class CommonDisease(models.Model):
    Disease = models.CharField(max_length=20, blank=False)
    Description = models.CharField(max_length=100, blank=False)
    Photo = models.CharField(blank=True, max_length=100)
    Solution = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.name
