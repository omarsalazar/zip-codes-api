from rest_framework import serializers
import pandas as pd
from api.federal_entities.v1.models import FederalEntityModel
from api.municipalities.v1.models import MunicipalityModel
from api.settlements.v1.models import SettlementModel, SettlementTypeModel
from api.zip_codes.v1.models import ZipCodeModel


class ZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipCodeModel
        fields = ('id', 'zip_code', 'locality', 'federal_entity', 'municipality')


class SettlementTypeZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettlementTypeModel
        fields = ("name",)


class SettlementZipCodeSerializer(serializers.ModelSerializer):
    settlement_type = SettlementTypeZipCodeSerializer()

    class Meta:
        model = SettlementModel
        fields = ('key', 'name', 'zone_type', 'settlement_type')


class FederalEntityZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FederalEntityModel
        fields = ("key", "name", "code")


class MunicipalityZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipalityModel
        fields = ("key", "name")


class ZipCodeListSerializer(serializers.ModelSerializer):
    settlements = serializers.SerializerMethodField()
    federal_entity = FederalEntityZipCodeSerializer()
    municipality = MunicipalityZipCodeSerializer()

    class Meta:
        model = ZipCodeModel
        fields = ('zip_code', 'locality', 'federal_entity', 'municipality', "settlements")

    def get_settlements(self, instance):
        settlements = SettlementModel.objects.filter(zip_code=instance.id)
        serialized_data = SettlementZipCodeSerializer(settlements, many=True)
        return serialized_data.data


class ZipCodeBulkCreateSerializer(serializers.Serializer):

    def get_valid_data_sheets(self, imported_data):
        imported_data_sheets = imported_data.sheet_names
        valid_data_sheets = [data_sheet for data_sheet in imported_data_sheets if data_sheet != "Nota"]
        return valid_data_sheets

    def get_file_data(self, file_data):
        imported_data = pd.ExcelFile(file_data.file)
        valid_data_sheets = self.get_valid_data_sheets(imported_data)
        return imported_data, valid_data_sheets

    def create(self, validated_data):
        imported_data, data_sheets = self.get_file_data(validated_data)
        try:
            for sheet in data_sheets:
                data = pd.read_excel(imported_data, sheet, dtype={"id_asenta_cpcons": str})
                for i in range(len(data)):
                    zip_code = str(data.get("d_codigo")[i])
                    locality = None if str(data.get("d_ciudad")[i]) == "nan" else str(data.get("d_ciudad")[i]).upper()
                    federal_entity_key = str(data.get("c_estado")[i])
                    federal_entity_name = str(data.get("d_estado")[i]).upper()
                    federal_entity_code = None if str(data.get("c_CP")[i]) == "nan" else str(data.get("c_CP")[i])
                    settlement_key = str(data.get("id_asenta_cpcons")[i])
                    settlement_name = str(data.get("d_asenta")[i])
                    settlement_zone_type = str(data.get("d_zona")[i])
                    settlement_type_name = str(data.get("d_tipo_asenta")[i]).upper()
                    municipality_key = str(data.get("c_mnpio")[i])
                    municipality_name = str(data.get("D_mnpio")[i])

                    municipality, municipality_is_created = MunicipalityModel.objects.get_or_create(
                        name=municipality_name, key=municipality_key)
                    settlement_type, settlement_type_is_created = SettlementTypeModel.objects.get_or_create(
                        name=settlement_type_name)
                    federal_entity, federal_entity_is_created = FederalEntityModel.objects.get_or_create(
                        key=federal_entity_key,
                        name=federal_entity_name,
                        code=federal_entity_code)
                    zip_code, zip_code_is_created = ZipCodeModel.objects.get_or_create(zip_code=zip_code,
                                                                                       locality=locality,
                                                                                       federal_entity=federal_entity,
                                                                                       municipality=municipality)
                    setttlement, setttlement_is_created = SettlementModel.objects.get_or_create(key=settlement_key,
                                                                                                name=settlement_name,
                                                                                                settlement_type=settlement_type,
                                                                                                zone_type=settlement_zone_type,
                                                                                                zip_code=zip_code)
            return {"status": 200, "message": "Batch created successfully"}
        except Exception as e:
            return {"status": "error", "message": e}

