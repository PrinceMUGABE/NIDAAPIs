from rest_framework import serializers
from .models import Rwandan

class RwandanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rwandan
        fields = '__all__'