from rest_framework import generics, permissions
from ...models import Blog, Category, Tag
from .serializers import BlogSerialzier, CategorySerializer, TagSerializer
from .permissions import IsOwnerOrReadOnly


class CategoryListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/blog/v1/category-list/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/blog/v1/tag-list/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BlogLIstCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-list-create/
    queryset = Blog.objects.all()
    serializer_class = BlogSerialzier

    # permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.request.method == ["GET"]:
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, ]
        return super(BlogLIstCreateAPIView, self).get_permissions()

    def get_queryset(self):
        qs = super(BlogLIstCreateAPIView, self).get_queryset()
        category = self.request.query_params.get('category')
        tags = self.request.query_params.get('tags')
        if category:
            qs = qs.filter(category__title=category)
        if tags:
            qs = qs.filter(tags__title=tags)
        return qs


class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/blog/v1/blog-rud/<id>/
    queryset = Blog.objects.all()
    serializer_class = BlogSerialzier
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
