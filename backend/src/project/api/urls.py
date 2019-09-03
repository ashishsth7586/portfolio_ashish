from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

router = DefaultRouter()
router.register('', ProjectViewSet, base_name='project_view')
urlpatterns = router.urls
