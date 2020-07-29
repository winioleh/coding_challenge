import factory
from django.contrib.auth import get_user_model
from faker import Factory
from wingtel.core.models import CustomUser, TelecommunicationCompany

User = get_user_model()

faker = Factory.create()


class CustomUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = CustomUser
    email = faker.ascii_free_email()
    first_name = faker.first_name()
    last_name = faker.last_name()
    is_active = True
    is_admin = False


class TelecommunicationCompanyFactory(factory.DjangoModelFactory):
    class Meta:
        model = TelecommunicationCompany
        django_get_or_create = ('name', 'website', 'one_kilobyte_price', 'one_second_price', 'network_type')