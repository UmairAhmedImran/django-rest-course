from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer


class PrdouctDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
