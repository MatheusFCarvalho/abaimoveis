
from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer

# Create your views here.


class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
