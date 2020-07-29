import factory
from django.contrib.auth import get_user_model
from faker import Factory
from wingtel.plans.models import Plan

User = get_user_model()

faker = Factory.create()


class PlanFactory(factory.DjangoModelFactory):
    class Meta:
        model = Plan
    name = faker.name()
    price = faker.pydecimal(left_digits=2, right_digits=2, positive=True)
    data_available = faker.random_int()
