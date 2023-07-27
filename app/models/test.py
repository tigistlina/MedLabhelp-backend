from django.db import models
from models.panel import Panel

# Create your models here.
class Test(models.Model):
    id = models.BigAutoField(primary_key=True)
    panel_id = models.ForeignKey(Panel, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    info_url = models.CharField(max_length=100)
    normal_reference = models.CharField(max_length=100)
    unit_of_measure = models.CharField(max_length=100)
