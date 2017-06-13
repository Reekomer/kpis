from .api import StoyoViewSet
from .api import PublisherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stoyo', StoyoViewSet)
router.register(r'publisher', PublisherViewSet)

urlpatterns = router.urls