from rest_framework import serializers

from .models import Settings

class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Settings
        fields = ('cube_power', 'light', 'heart', 'gender', 'sadness', 'wifi', 'temperature', 'water', 'tv', 'weather')