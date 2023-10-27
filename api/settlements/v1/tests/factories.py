import factory


class SettlementTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "settlements.SettlementTypeModel"
        django_get_or_create = ('name',)

    name = factory.Faker("word")


class SettlementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "settlements.SettlementModel"
        django_get_or_create = ('name', )

    name = factory.Faker("word")

