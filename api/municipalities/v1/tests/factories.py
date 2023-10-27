import factory


class MunicipalityFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "municipalities.MunicipalityModel"
        django_get_or_create = ('name',)

    name = factory.Faker("word")
    key = factory.Faker("word")
