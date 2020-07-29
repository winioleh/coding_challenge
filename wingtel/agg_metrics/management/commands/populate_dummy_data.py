import random
import logging

from django.core.management.base import BaseCommand

from wingtel.subscriptions.tests.factories.subscriptions import SubscriptionFactory
from wingtel.plans.tests.factories.plan import PlanFactory
from wingtel.core.tests.factories.core import TelecommunicationCompanyFactory, CustomUserFactory
from wingtel.usage.tests.factories.usage import UsageRecordsFactory


logg = logging.getLogger('general')


class Command(BaseCommand):
    help = 'Populate aggregated usage models with data from the raw usage models'

    def handle(self, *args, **options):
        self.stdout.write("Unterminated line", ending='')
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

        users = []
        subscriptions = []
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
        from faker import Factory
        faker = Factory.create()
        for _ in range(100):
            usage_record = UsageRecordsFactory(
                subscription=random.choice(subscriptions),
                usage_type=random.choice(['data', 'voice']),
                usage_date=faker.date_this_month()
            )
            usage_records.append(usage_record)
