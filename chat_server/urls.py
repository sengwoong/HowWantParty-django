from django.urls import path, include
from .views import ChatbotAPIView,MessageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'admin', MessageViewSet)
urlpatterns = [
	path('', ChatbotAPIView.as_view(), name='chat'),
    path('all', include(router.urls)),
]


