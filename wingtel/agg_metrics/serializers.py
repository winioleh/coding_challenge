from rest_framework import serializers

from wingtel.agg_metrics.models import AggUsageRecordsDay


class AggUsageRecordsDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = AggUsageRecordsDay
        fields = '__all__'
