from django.db import models
from app.models.panel import Panel

# Create your models here.
class Test(models.Model):
    # id = models.BigAutoField(primary_key=True)
    panel_id = models.ForeignKey(Panel, on_delete=models.CASCADE, null=True)
    name = models.TextField()
    description = models.TextField()
    info_url = models.TextField()
    normal_reference = models.TextField()
    unit_of_measure = models.TextField()
