from rest_framework import serializers
import re
from .models import CommonDisease


class CommonDiseaseSerializer(serializers.ModelSerializer):
    Disease = serializers.CharField(min_length=3)

    class Meta:
        model = CommonDisease
        fields = ['Disease']

    def create(self, validated_data):
        disease = CommonDisease.objects.filter(Disease=validated_data['Disease'])
        if disease:
            raise serializers.ValidationError('Disease already exists')
        if not re.match("^[A-Za-z]", validated_data['Disease']):
            raise serializers.ValidationError('Invalid input provided')
        else:
            return CommonDisease.objects.create(**validated_data)

