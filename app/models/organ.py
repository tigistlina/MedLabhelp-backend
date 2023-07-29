from django.db import models

# Create your models here.
class Organ(models.Model):
    name = models.TextField()

    @classmethod
    def from_dict(cls, data_dict):

        return cls(
            name = data_dict["name"],
        )
