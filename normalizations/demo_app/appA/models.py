
from django.db import models

class ModelA(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    complete_name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.complete_name = f"{self.fname}_{self.lname}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.complete_name