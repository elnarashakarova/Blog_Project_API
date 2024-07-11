from rest_framework import generics, permissions
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer
from .permission import IsOwnerOrReadOnly

# Create your views here.
class PostListCreate(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentCreate(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])
        
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['post_pk'])
        
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])
    serializer_class = CommentSerializer
    