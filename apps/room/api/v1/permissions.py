from django.urls import path, include


urlpatterns = [
    path('v1/', include('apps.room.api.v1.urls'))
]