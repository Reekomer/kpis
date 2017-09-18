from .api import StoyoViewSet
from .api import PublisherViewSet
from .api import TemporaryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stoyo', StoyoViewSet)
router.register(r'publisher', PublisherViewSet)
router.register(r'temporary', TemporaryViewSet)

urlpatterns = router.urls
