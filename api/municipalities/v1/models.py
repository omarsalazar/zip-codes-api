from django.db import models


class MunicipalityModel(models.Model):
    key = models.CharField()
    name = models.CharField()

    def __str__(self):
        return self.name
