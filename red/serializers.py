from rest_framework import serializers

from .models import ComputerScienceEducatorsPost, CseEndeavour


class ComputerScienceEducatorsPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ComputerScienceEducatorsPost


class CseEndeavourSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CseEndeavour
