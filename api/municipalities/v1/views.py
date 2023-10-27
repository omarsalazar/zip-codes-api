from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from api.municipalities.v1.models import MunicipalityModel
from api.municipalities.v1.serializers import MunicipalitySerializer


class MunicipalityViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    queryset = MunicipalityModel.objects.all()
    serializer_class = MunicipalitySerializer
    permission_classes = (IsAuthenticated,)


class MunicipalityCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = MunicipalityModel.objects.all()
    serializer_class = MunicipalitySerializer
    permission_classes = (IsAuthenticated,)
