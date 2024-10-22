from django.shortcuts import render
from apps.settings.models import Settings
from apps.settings.serializers import SettingsSerializers
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
# Create your views here.

class SettingsAPI(GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializers