from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    imagens = serializers.ListField(
        child=serializers.ImageField(),
        required=False
    )

    class Meta:
        model = Property
        fields = "__all__"

    def validate_cep(self, value):
        if not value.isdigit() or len(value) != 8:
            raise serializers.ValidationError("CEP inválido.")
        return value
