from rest_framework import serializers

from api.settlements.v1.models import SettlementModel, SettlementTypeModel


class SettlementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettlementTypeModel
        fields = ('id', 'name')


class SettlementSerializer(serializers.ModelSerializer):

    class Meta:
        model = SettlementModel
        fields = ('id', 'key', 'name', 'zone_type', 'settlement_type', 'zip_code')
