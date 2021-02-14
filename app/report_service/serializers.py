from rest_framework import serializers
from .models import StatElement

class StatElementSerializer(serializers.ModelSerializer):
    element = serializers.CharField(source='get_element_display')
    score = serializers.CharField(source='get_score_display')

    class Meta:
        model = StatElement
        fields = ['id', 'element', 'score', 'subject', 'student', 'teacher']


class StatElementUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatElement
        fields = ['id', 'element', 'score', 'subject', 'student', 'teacher']

