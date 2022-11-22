from rest_framework import viewsets, permissions
from ...models import About, Service
from .serializers import MarianSerializer


class AboutViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/api/main/v1/about/<id>/
    queryset = About.objects.all()
    serializer_class = MarianSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        MarianSerializer().set_model(About)
        return serializer


class ServiceViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/api/main/v1/service/<id>/
    queryset = Service.objects.all()
    serializer_class = MarianSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        MarianSerializer().set_model(Service)
        return serializer
