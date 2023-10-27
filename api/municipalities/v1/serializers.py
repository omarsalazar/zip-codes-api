from rest_framework import serializers

from api.municipalities.v1.models import MunicipalityModel


class MunicipalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = MunicipalityModel
        fields = ('id', 'key', 'name')
