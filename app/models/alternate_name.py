from django.db import models
from models.test import Test

# Create your models here.
class AlternateName(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_id = models.ForeignKey(Test, null=True)
    name = models.CharField(max_length=100)