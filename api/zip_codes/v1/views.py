from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from api.zip_codes.v1.models import ZipCodeModel
from api.zip_codes.v1.serializers import ZipCodeSerializer, ZipCodeListSerializer, ZipCodeBulkCreateSerializer


class ZipCodeCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ZipCodeModel.objects.all()
    serializer_class = ZipCodeSerializer
    permission_classes = (IsAuthenticated,)


class ZipCodeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ZipCodeModel.objects.all()
    serializer_class = ZipCodeListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        params = self.request.query_params.get("zip-code")
        if params is not None:
            return ZipCodeModel.objects.filter(zip_code=params)
        else:
            return self.queryset


def zip_code_bulk_upload(request):
    if request.method == 'POST':
        uploaded_file_data = request.FILES.get("file")
        serializer = ZipCodeBulkCreateSerializer()
        resp = serializer.create(uploaded_file_data)
        return JsonResponse(resp)

    return render(request, "upload_page.html")
