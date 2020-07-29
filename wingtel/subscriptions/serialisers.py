from rest_framework import serializers

from wingtel.subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ["user", "plan", "status", "device_id", "phone_number",
                  "phone_model", "provider_company", "effective_date"]
