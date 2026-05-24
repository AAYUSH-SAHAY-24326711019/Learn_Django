from django.db import models

class ModelB(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name