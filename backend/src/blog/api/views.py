from rest_framework import viewsets
from ..models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer
