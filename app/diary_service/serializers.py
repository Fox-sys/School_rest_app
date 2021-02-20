from rest_framework import serializers
from .models import Subject, Group, Homework

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'teacher', 'name', 'description']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'students', 'curator', 'subjects', 'homework']
        read_only_fields = ['name', 'students', 'curator', 'subjects']


class HomeworkSerializer(serializers.ModelSerializer):
    score = serializers.CharField(source='get_score_display')

    class Meta:
        model = Homework
        fields = ['id', 'short_desc', 'full_desc', 'teacher', 'start_date', \
                  'end_date', 'pins', 'score', 'subject']


class HomeworkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ['id', 'short_desc', 'full_desc', 'teacher', \
                  'end_date', 'pins', 'score', 'subject']


class HomeworkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ['id', 'short_desc', 'full_desc', 'end_date', 'pins', 'score']