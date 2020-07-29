import factory
from faker import Factory
from wingtel.subscriptions.models import Subscription
from wingtel.core.tests.factories.core import CustomUserFactory, TelecommunicationCompanyFactory
from wingtel.plans.tests.factories.plan import PlanFactory

faker = Factory.create()
# user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
#     plan = models.ForeignKey(Plan, null=True, on_delete=models.PROTECT)
#     status = models.CharField(max_length=10, choices=STATUS, default=STATUS.new)
#     device_id = models.CharField(max_length=20, default='')
#     phone_number = models.CharField(max_length=20, default='')
#     phone_model = models.CharField(max_length=128, default='')
#     provider_company = models.ForeignKey(TelecommunicationCompany, on_delete=models.PROTECT)
#     effective_date = models.DateTimeField(null=True)


class SubscriptionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Subscription
    user = factory.SubFactory(CustomUserFactory)
    plan = factory.SubFactory(PlanFactory)
    device_id = faker.pystr(max_chars=20)
    phone_number = faker.pystr(max_chars=20)
    phone_model = faker.pystr(max_chars=128)
    provider_company = factory.SubFactory(TelecommunicationCompanyFactory)