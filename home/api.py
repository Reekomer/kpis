from rest_framework.viewsets import ModelViewSet

from .serializers import StoyoSerializer
from .serializers import PublisherSerializer
from .serializers import TemporarySerializer

from .models import Stoyo
from .models import Publisher
from .models import Temporary

class StoyoViewSet(ModelViewSet):
    queryset = Stoyo.objects.all()
    serializer_class = StoyoSerializer

class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class TemporaryViewSet(ModelViewSet):
    queryset = Temporary.objects.all()
    serializer_class = TemporarySerializer
