from django.contrib import admin

from api.settlements.v1.models import SettlementModel
from api.zip_codes.v1.models import ZipCodeModel


class SettlementInline(admin.TabularInline):
    model = SettlementModel
    extra = 1


@admin.register(ZipCodeModel)
class ZipCodeAdmin(admin.ModelAdmin):
    inlines = [SettlementInline]


