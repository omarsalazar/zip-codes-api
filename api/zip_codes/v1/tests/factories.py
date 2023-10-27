import factory

from api.federal_entities.v1.tests.factories import FederalEntityFactory
from api.municipalities.v1.tests.factories import MunicipalityFactory


class ZipCodeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "zip_codes.ZipCodeModel"
        django_get_or_create = ('zip_code',)

    zip_code = factory.Faker("word")
    locality = factory.Faker("word")
    # federal_entity = factory.SubFactory(FederalEntityFactory)
    federal_entity = factory.Faker("random_int")
    # municipality = factory.SubFactory(MunicipalityFactory)
    municipality = factory.Faker("random_int")
