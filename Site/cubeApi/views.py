from rest_framework import viewsets

from .serializer import SettingsSerializer
from .models import Settings

class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all().order_by('cube_power')
    serializer_class = SettingsSerializer