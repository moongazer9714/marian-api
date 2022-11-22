from django.urls import path
from .views import ContactCreateAPIView, ContactRetrieveDestroyAPIView


urlpatterns = [
    path('contact-create/', ContactCreateAPIView.as_view()),
    path('contact-rd/<int:pk>/', ContactRetrieveDestroyAPIView.as_view()),
]