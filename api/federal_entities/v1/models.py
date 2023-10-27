from django.db import models


class FederalEntityModel(models.Model):
    key = models.CharField()
    name = models.CharField()
    code = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name
