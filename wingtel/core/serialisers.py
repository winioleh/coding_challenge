from rest_framework import serializers

from wingtel.core.models import CustomUser, TelecommunicationCompany


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "is_admin", "is_active", "id"]


class TCSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelecommunicationCompany
        fields = ["status", "name", "one_kilobyte_price", "one_second_price", "network_type", "id"]
