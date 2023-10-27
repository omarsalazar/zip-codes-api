from django.contrib import admin

from api.municipalities.v1.models import MunicipalityModel


@admin.register(MunicipalityModel)
class MunicipalityAdmin(admin.ModelAdmin):
    pass
