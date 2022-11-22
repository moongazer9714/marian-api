from django.urls import path
from .views import CommentListCreateView, CommentDeleteView

urlpatterns = [
    path('<int:blog_id>/list-create/', CommentListCreateView.as_view()),
    path('<int:blog_id>/delete/<int:pk>/', CommentDeleteView.as_view()),
]
