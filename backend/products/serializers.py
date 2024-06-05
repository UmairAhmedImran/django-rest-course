from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'title', 'content', 'sales_price', 'discount']

    def get_discount(self, obj):
        return obj.get_discount()
