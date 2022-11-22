from rest_framework import serializers

from apps.accounts.api.v1.serializers import AccountUpdateSerializer
from apps.blog.api.v1.serializers import BlogSerialzier
from ...models import Comment


class CommentSubSerializer(serializers.ModelSerializer):
    author = AccountUpdateSerializer(read_only=True, required=False)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'parent', 'message', 'is_reply', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    author = AccountUpdateSerializer(read_only=True, required=False)
    blog = BlogSerialzier(read_only=True, required=False)
    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, obj):
        try:
            comments = Comment.objects.filter(top_level_comment_id=obj.id).exclude(id=obj.id)
        except:
            return []
        else:
            serializer = CommentSubSerializer(comments, many=True)
            return serializer.data

    class Meta:
        model = Comment
        fields = (
            'id', 'author', 'parent', 'blog', 'top_level_comment_id', 'message', 'is_reply', 'children', 'created_at')
        extra_kwargs = {
            'author': {'required': False, 'allow_null': True},
            'parent': {'required': False},
            'blog': {'required': False, 'allow_null': True},
            'top_level_comment_id': {'required': False, 'allow_null': True, 'read_only': True},
            'is_reply': {'required': False, 'allow_null': True, 'read_only': True},
            'created_at': {'required': False, 'allow_null': True},
        }
