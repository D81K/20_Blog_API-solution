from rest_framework import serializers
from .models import Category, Post, Comment, Like, PostView


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'post',
            'time_stamp',
            'content',
        )

        extra_kwargs = {
            'user': {'read_only': True}
        }


class PostSerializer (serializers.ModelSerializer):

    author = serializers.StringRelatedField()
    author_id = serializers.IntegerField(read_only=True)
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField(required=True)

    has_like = serializers.SerializerMethodField()

    def get_has_like(self, obj):
        request = self.context.get('request')
        if request.user.is_authenticated:
            if Like.objects.filter(user=request.user, post=obj).exists():
                return True
        return False
    
    def get_isowner(self, obj):
        request = self.context.get('request')
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
        return False
    
    class Meta:
        model = Post
        fields = '__all__'

        extra_kwargs = {
            'author': {'read_only': True}
        }
    


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'