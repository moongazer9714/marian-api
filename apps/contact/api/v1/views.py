from rest_framework import generics, permissions
from .serializers import ContactSerializer
from ...models import Contact


class ContactCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/api/contact/v1/contact-create/
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]


class ContactRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    # http://127.0.0.1:8000/api/contact/v1/contact-rd/<id>/
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]
