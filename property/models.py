# property/models.py
from django.contrib.postgres.fields import ArrayField
from django.db import models
from address.models import Address
import uuid


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    imagens = ArrayField(models.BinaryField(), blank=True, null=True)
    descricao = models.TextField()
