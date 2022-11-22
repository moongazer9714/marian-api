from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'service', ServiceViewSet)


urlpatterns = [
    path('', include(router.urls))
]
