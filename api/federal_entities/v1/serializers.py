from rest_framework import serializers

from api.federal_entities.v1.models import FederalEntityModel


class FederalEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = FederalEntityModel
        fields = ('id', 'key', 'name', 'code')
