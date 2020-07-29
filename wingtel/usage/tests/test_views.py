import pytest
import random

from django.urls import reverse
from django.test import Client
from faker import Factory

from wingtel.core.tests.factories.core import CustomUserFactory, TelecommunicationCompanyFactory
from wingtel.usage.tests.factories.usage import UsageRecordsFactory
from wingtel.plans.tests.factories.plan import PlanFactory
from wingtel.subscriptions.tests.factories.subscriptions import SubscriptionFactory

faker = Factory.create()
web_client = Client()


@pytest.mark.django_db
def test_get_subscriptions_with_exceeded_price_limit():
    url = reverse('subscription_exceeded_price_limit')
    response = web_client.get(url, data={
        'price_limit': 50
    }).json()
    assert len(response) == 0
    att_provider = TelecommunicationCompanyFactory(
        name="ATT",
        website="https://att.com",
        one_kilobyte_price=0.001,
        one_second_price=0.001,
        network_type="LAN"
    )
    sprint_provider = TelecommunicationCompanyFactory(
        name="Sprint",
        website="https://sprint.com",
        one_kilobyte_price=0.0015,
        one_second_price=0.0015,
        network_type="LAN"

    )
    providers = [sprint_provider, att_provider]
    plans = [PlanFactory() for _ in range(10)]
    subscriptions = []
    users = []
    for _ in range(20):
        user = CustomUserFactory()
        subscription = SubscriptionFactory(
            user=user,
            plan=random.choice(plans),
            provider_company=random.choice(providers),
        )
        users.append(user)
        subscriptions.append(subscription)
    usage_records = []
    for _ in range(100):
        usage_record = UsageRecordsFactory(
            subscription=random.choice(subscriptions),
            usage_type=random.choice(['data', 'voice']),
            usage_date=faker.date_this_month(),
            price=55
        )
        usage_records.append(usage_record)
    response = web_client.get(url, data={
        'price_limit': 50
    }).json()
    assert len(response) == len(usage_records)