from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from api.settlements.v1.models import SettlementTypeModel, SettlementModel
from api.settlements.v1.serializers import SettlementTypeSerializer, SettlementSerializer



class SettlementTypeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    queryset = SettlementTypeModel.objects.all()
    serializer_class = SettlementTypeSerializer
    permission_classes = (IsAuthenticated,)


class SettlementTypeCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SettlementTypeModel.objects.all()
    serializer_class = SettlementTypeSerializer
    permission_classes = (IsAuthenticated,)


class SettlementCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SettlementModel.objects.all()
    serializer_class = SettlementSerializer
    permission_classes = (IsAuthenticated,)


class SettlementViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = SettlementModel.objects.all()
    serializer_class = SettlementSerializer
    permission_classes = (IsAuthenticated,)
