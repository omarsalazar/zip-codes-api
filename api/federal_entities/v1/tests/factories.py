import factory


class FederalEntityFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "federal_entities.FederalEntityModel"
        django_get_or_create = ('name',)

    name = factory.Faker("word")
    key = factory.Faker("word")
