from django.db import models
from models.organ import Organ

# Create your models here.
class Panel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    organ_id = models.ForeignKey(Organ, null=True)
    