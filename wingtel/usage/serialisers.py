from rest_framework import serializers

from wingtel.usage.models import UsageRecord


class UsageRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsageRecord
        fields = '__all__'