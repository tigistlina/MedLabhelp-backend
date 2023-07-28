from django.db import models
from app.models.panel import Panel

# Create your models here.
class Test(models.Model):
    panel_id = models.ForeignKey(Panel, on_delete=models.CASCADE, null=True)
    name = models.TextField()
    description = models.TextField()
    info_url = models.TextField()
    normal_reference = models.TextField()
    unit_of_measure = models.TextField()

class AlternateName(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    name = models.TextField()
