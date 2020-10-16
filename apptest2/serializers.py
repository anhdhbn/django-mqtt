from rest_framework import serializers

from .models import Temp

class TempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temp
        fields = ('env_temp', 'obj_temp', 'distance')