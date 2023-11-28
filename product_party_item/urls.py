from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()


# 'product'에 대한 API 뷰셋 등록
router.register(r'product', views.ProductViewSet)
# 'imgs'에 대한 API 뷰셋 등록
router.register(r'imgs', views.ProductImgViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
