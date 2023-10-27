from django.db import models

from api.federal_entities.v1.models import FederalEntityModel
from api.municipalities.v1.models import MunicipalityModel


class ZipCodeModel(models.Model):
    zip_code = models.CharField()
    locality = models.CharField(null=True, blank=True)
    federal_entity = models.ForeignKey(FederalEntityModel, on_delete=models.DO_NOTHING)
    municipality = models.ForeignKey(MunicipalityModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.municipality.name}-{self.zip_code}"
