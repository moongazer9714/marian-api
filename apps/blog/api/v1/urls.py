from django.urls import path
from .views import CategoryListView, TagListView, BlogLIstCreateAPIView, BlogRetrieveUpdateDestroyView

urlpatterns = [
    path('category-list/', CategoryListView.as_view()),
    path('tag-list/', TagListView.as_view()),
    path('blog-list-create/', BlogLIstCreateAPIView.as_view()),
    path('blog-rud/<int:pk>/', BlogRetrieveUpdateDestroyView.as_view()),
]