from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    def validate_cep(self, value):
        if not value.isdigit() or len(value) != 8:
            raise serializers.ValidationError("CEP inválido.")
        return value
