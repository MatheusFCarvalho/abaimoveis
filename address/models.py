from django.db import models
from django.core.validators import RegexValidator
import uuid

# Create your models here.


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cep = models.CharField(max_length=8, validators=[
                           RegexValidator(r'^\d{8}$', 'CEP inválido')])
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    number = models.PositiveIntegerField(blank=True, null=True)
