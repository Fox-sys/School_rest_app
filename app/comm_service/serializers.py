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
        fields = ['id', 'author', 'replies_to', 'text', 'pins', 'date', 'is_edited']
        read_only_fields = ['author', 'date', 'is_edited']        

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.is_edited = True
        instance.save()
        return instance