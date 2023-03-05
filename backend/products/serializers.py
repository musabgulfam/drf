from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'discount',
        ]

    def get_discount(self, obj):
        try:
            return obj.discount_price
        except:
            return None