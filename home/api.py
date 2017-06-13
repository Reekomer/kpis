from rest_framework.viewsets import ModelViewSet

from .serializers import StoyoSerializer
from .serializers import PublisherSerializer

from .models import Stoyo
from .models import Publisher

class StoyoViewSet(ModelViewSet):
    queryset = Stoyo.objects.all()
    serializer_class = StoyoSerializer

class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer