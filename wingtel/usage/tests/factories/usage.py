import factory
from faker import Factory
from wingtel.usage.models import UsageRecord
from wingtel.subscriptions.tests.factories.subscriptions import SubscriptionFactory

faker = Factory.create()


class UsageRecordsFactory(factory.DjangoModelFactory):
    class Meta:
        model = UsageRecord
    subscription = factory.SubFactory(SubscriptionFactory)
    price = faker.pydecimal(left_digits=1, right_digits=2, positive=True)
    usage_date = faker.date_this_month()
    usage_type = faker.pystr(max_chars=20)
    resource_used = faker.pyint(min_value=1)
