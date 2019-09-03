from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register('', BlogViewSet, base_name='blog_view')
urlpatterns = router.urls
