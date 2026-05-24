from django.db import models
from appA.models import ModelA
from appB.models import ModelB

class MainModel(models.Model):
    emp = models.ForeignKey(ModelA, on_delete=models.CASCADE)
    dept = models.ForeignKey(ModelB, on_delete=models.CASCADE)