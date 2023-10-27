from django.contrib import admin

from api.settlements.v1.models import SettlementTypeModel, SettlementModel


@admin.register(SettlementTypeModel)
class SettlementTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(SettlementModel)
class SettlementAdmin(admin.ModelAdmin):
    pass
