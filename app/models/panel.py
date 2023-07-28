from django.db import models
from app.models.organ import Organ

# Create your models here.
class Panel(models.Model):
    name = models.TextField()
    organ_id = models.ForeignKey(Organ, null=True, blank=True, on_delete=models.SET_NULL)
