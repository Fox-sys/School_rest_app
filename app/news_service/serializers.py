from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    news_type = serializers.CharField(source='get_news_type_display')
    class Meta:
        model = News
        fields = ['id', 'news_type', 'title', 'info', 'subject_from', 'subject_to']

class NewsUpdateCreateSerializer(NewsSerializer):
    types = ('rp', 'nw', 'an')
    news_type = serializers.CharField()

    def create(self, validated_data):
        if not validated_data.get('news_type', None) in self.types:
            raise serializers.ValidationError("Передан несуществующий тип новостей")
        return super().create(validated_data)


    def update(self, inctance, validated_data):
        news_type = validated_data.get('news_type', None)
        if not news_type in self.types and news_type:
            raise serializers.ValidationError("Передан несуществующий тип новостей")
        return super().update(inctance, validated_data)