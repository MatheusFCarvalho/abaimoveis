from rest_framework import serializers
from .models import Property
from address.serializers import AddressSerializer
from address.models import Address


class PropertySerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        required=False
    )
    address = AddressSerializer()

    class Meta:
        model = Property
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        address = Address.objects.create(**address_data)
        validated_data["address"] = address
        property = Property.objects.create(**validated_data)
        return property

    def validate_cep(self, value):
        if not value.isdigit() or len(value) != 8:
            raise serializers.ValidationError("CEP inválido.")
        return value
