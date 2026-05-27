from django.db import models

# Create your models here.
class Faculty(models.Model):
    fname = models.CharField(max_length=100)

    def __str__(self):
        return self.fname
