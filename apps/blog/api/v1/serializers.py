from rest_framework import serializers

from apps.accounts.api.v1.serializers import AccountUpdateSerializer
from ...models import Blog, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class BlogSerialzier(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title', read_only=True)
    tag_names = serializers.SerializerMethodField(required=False, read_only=True)
    author = AccountUpdateSerializer(read_only=True, required=False)

    def get_tag_names(self, obj):
        tags = obj.tags.all()
        data = []
        for i in tags:
            data.append({'title': i.title})
        return data

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'image', 'description', 'category', 'category_name', 'tags', 'tag_names',
                  'created_at']
        extra_kwargs = {
            'tag_names': {'requires': False}
        }

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        user = self.context['request'].user
        blog = Blog.objects.create(author_id=user.id, **validated_data)
        for tag in tags:
            blog.tags.add(tag)
        return blog

    def validate(self, attrs):
        user = self.context['request'].user
        title = attrs.get('title')
        blog = Blog.objects.filter(title__icontains=title, author_id=user.id)
        if blog:
            raise serializers.ValidationError('title must be unique')
        return attrs

