from rest_framework import serializers
from .models import Chat, Message

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'members', 'curator', 'is_curated', 'messages']
        read_only_fields = ['name', 'members', 'curator', 'is_curated']   
        

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'replays_to', 'text', 'pins', 'date', 'is_edited']
        read_only_fields = ['author', 'date', 'is_edited']        

    def update(self, instance, validated_data):
        instance.replays_to = validated_data.get('replays_to', instance.replays_to)
        instance.text = validated_data.get('text', instance.text)
        instance.pins = validated_data.get('pins', instance.pins)
        instance.is_edited = True
        instance.save()
        return instance