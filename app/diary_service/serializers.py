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
        read_only_fields = ['teacher', 'start_date', 'subject', 'pins']


class HomeworkUpdateSerializer(HomeworkSerializer):
    scores = ['1', '2', '3', '4']
    score = serializers.CharField()
    
    def create(self, validated_data):
        if not validated_data.get('score', None) in self.scores:
            raise serializers.ValidationError("Передан несуществующий балл")
        return super().create(validated_data)


    def update(self, inctance, validated_data):
        score = validated_data.get('score', None)
        if not score in self.scores and score:
            raise serializers.ValidationError("Передан несуществующий балл")
        return super().update(inctance, validated_data)