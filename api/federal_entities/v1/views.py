from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from api.federal_entities.v1.models import FederalEntityModel
from api.federal_entities.v1.serializers import FederalEntitySerializer


class FederalEntityViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    queryset = FederalEntityModel.objects.all()
    serializer_class = FederalEntitySerializer
    permission_classes = (IsAuthenticated,)


class FederalEntityCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = FederalEntityModel.objects.all()
    serializer_class = FederalEntitySerializer
    permission_classes = (IsAuthenticated,)
