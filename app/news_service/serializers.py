from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    news_type = serializers.CharField(source='get_news_type_display')
    class Meta:
        model = News
        fields = ['id', 'news_type', 'title', 'info', 'subject_from', 'subject_to']

class NewsUpdateCreateSerializer(serializers.ModelSerializer):
    types = ('rp', 'nw', 'an')

    class Meta:
        model = News
        fields = ['id', 'news_type', 'title', 'info', 'subject_from', 'subject_to']

    def create(self, validated_data):
        self.validate_subject_fields(validated_data)
        return super().create(validated_data)

    def update(self, inctance, validated_data):
        self.validate_subject_fields(validated_data)
        return super().update(inctance, validated_data)
    
    def validate_subject_fields(self, validated_data):
        news_type = validated_data.get('news_type', None)
        subject_from = validated_data.get('subject_from', None)
        subject_to = validated_data.get('subject_to', None)
        if not news_type == 'rp' and (subject_from or subject_to) and (news_type or subject_to or subject_from):
            raise serializers.ValidationError('Нельзя передавать предметы, если тип новости не является заменой')
        if news_type == 'rp' and not (subject_from and subject_to) and (news_type or subject_to or subject_from):
            raise serializers.ValidationError('Не были переданны обязательные предметы замены')
