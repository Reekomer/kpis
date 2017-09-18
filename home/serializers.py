from rest_framework import serializers
from .models import Stoyo
from .models import Publisher
from .models import Temporary

class StoyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stoyo

class PublisherSerializer(serializers.ModelSerializer):
    datepub = serializers.DateField(required=False)
    update = serializers.DateTimeField(required=False)
    page_name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    link = serializers.CharField(required=False)
    class Meta:
        model = Publisher

class TemporarySerializer(serializers.ModelSerializer):
    datepub = serializers.DateField(required=False)
    update = serializers.DateTimeField(required=False)
    page_name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    link = serializers.CharField(required=False)
    class Meta:
        model = Temporary
