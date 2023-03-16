# property/models.py
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from django.db import models
import uuid


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cep = models.CharField(max_length=8, validators=[
                           RegexValidator(r'^\d{8}$', 'CEP inválido')])
    logradouro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    preco = models.PositiveIntegerField
    estado = models.CharField(max_length=2)
    numero = models.PositiveIntegerField(blank=True)
    imagens = ArrayField(models.BinaryField(), blank=True, null=True)
    descricao = models.TextField()



