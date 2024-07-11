from rest_framework import serializers
from .models import Post, Comment
from blog_project.utils import sanitize_html

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    content = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = '__all__'
    
    def validate_description(self, value):
        return sanitize_html(value)
    
        
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    content = serializers.StringRelatedField()
    
    class Meta:
        model = Comment
        fields = '__all__'
    
    def validate_description(self, value):
        return sanitize_html(value)