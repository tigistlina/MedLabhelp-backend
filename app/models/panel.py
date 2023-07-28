from django.db import models
from app.models.organ import Organ

# Create your models here.
class Panel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    organ_id = models.ForeignKey(Organ, on_delete=models.CASCADE, null=True)
    