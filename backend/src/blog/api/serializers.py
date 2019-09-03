from ..models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        depth = 1
