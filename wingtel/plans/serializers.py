from rest_framework import serializers

from wingtel.plans.models import Plan


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ['name', 'price', 'data_available', "id"]