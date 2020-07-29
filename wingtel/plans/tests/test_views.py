from django.urls import reverse
from faker import Factory
import pytest
from .factories.plan import PlanFactory
from django.test import Client

faker = Factory.create()
web_client = Client()


@pytest.mark.django_db
def test_plans_view_list():
    plans = [PlanFactory() for _ in range(10)]
    url = reverse('api:plans-list')
    response = web_client.get(url).json()
    assert len(plans) == len(response)