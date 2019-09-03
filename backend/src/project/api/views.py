from rest_framework import viewsets
from ..models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all().order_by('-title')
    serializer_class = ProjectSerializer
