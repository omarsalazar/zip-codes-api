from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .federal_entities.v1.views import FederalEntityCreateViewSet, FederalEntityViewSet
from .municipalities.v1.views import MunicipalityViewSet, MunicipalityCreateViewSet
from .settlements.v1.views import SettlementTypeViewSet, SettlementTypeCreateViewSet, SettlementCreateViewSet, \
    SettlementViewSet
from .users.views import UserViewSet, UserCreateViewSet
from .zip_codes.v1.views import ZipCodeCreateViewSet, ZipCodeViewSet, zip_code_bulk_upload

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'settlements/settlement-types', SettlementTypeViewSet)
router.register(r'settlements/settlement-type', SettlementTypeCreateViewSet)
router.register(r'settlement', SettlementCreateViewSet)
router.register(r'settlements', SettlementViewSet)
router.register(r'federal-entities', FederalEntityViewSet)
router.register(r'federal-entity', FederalEntityCreateViewSet)
router.register(r'municipalities', MunicipalityViewSet)
router.register(r'municipality', MunicipalityCreateViewSet)
router.register(r'zip-code', ZipCodeCreateViewSet, basename='zipcode')
router.register(r'zip-codes', ZipCodeViewSet)
# router.register(r'zip-codes/bulk', zip_code_bulk_upload, basename="zipcode-bulk")

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include(router.urls)),
                  path('api-token-auth/', views.obtain_auth_token),
                  path('zip-codes/bulk/', zip_code_bulk_upload),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                  # the 'api-root' from django rest-frameworks default router
                  # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
                  re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
