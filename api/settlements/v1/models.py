from django.db import models

from api.zip_codes.v1.models import ZipCodeModel


class SettlementTypeModel(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class SettlementModel(models.Model):
    key = models.CharField()
    name = models.CharField()
    zone_type = models.CharField()
    settlement_type = models.ForeignKey(SettlementTypeModel, on_delete=models.DO_NOTHING)
    zip_code = models.ForeignKey(ZipCodeModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
