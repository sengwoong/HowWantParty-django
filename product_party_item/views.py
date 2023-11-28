
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer,ProductImageSerializer
# from ..blog.permissions import IsAuthorOrReadOnly

# product_party_item/views.py
from django.shortcuts import render
from .models import Product,ProductImage


# Your views and other code here

class ProductViewSet(ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    # permission_classes = [IsAuthorOrReadOnly]


class ProductImgViewSet(ModelViewSet):
    
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer 
    # permission_classes = [IsAuthorOrReadOnly]

