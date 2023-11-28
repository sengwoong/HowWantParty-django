from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)  # Assuming 'image' is the field you want to include

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True, source='product_id')  # Use the correct source

    class Meta:
        model = Product
        fields = '__all__'
