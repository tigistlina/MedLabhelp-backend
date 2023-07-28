from django.db import models
from app.models.test import Test

# Create your models here.
class AlternateName(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    name = models.TextField()