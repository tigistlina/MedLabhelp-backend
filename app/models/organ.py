from django.db import models

# Create your models here.
class Organ(models.Model):
    # id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    