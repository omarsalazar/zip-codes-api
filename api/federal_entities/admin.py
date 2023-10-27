from django.contrib import admin

from api.federal_entities.v1.models import FederalEntityModel


@admin.register(FederalEntityModel)
class FederalEntityAdmin(admin.ModelAdmin):
    pass

