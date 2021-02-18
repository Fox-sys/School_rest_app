from rest_framework import serializers
from .models import Chat, Message
from django.shortcuts import get_object_or_404

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'members', 'curator', 'is_curated', 'messages']
        read_only_fields = ['name', 'members', 'curator', 'is_curated']   
        

class MessageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'replies_to', 'text', 'pins', 'date', 'is_edited']
        read_only_fields = ['author', 'date', 'is_edited']        

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.is_edited = True
        instance.save()
        return instance

class MessageCreateSerializer(serializers.ModelSerializer):
    chat = serializers.CharField()

    class Meta:
        model = Message
        fields = ['id', 'author', 'replies_to', 'text', 'pins', 'chat']
    
    def create(self, validated_data):
        chat = get_object_or_404(Chat, id=validated_data.get('chat'))
        message = super().create(validated_data)
        chat.messages.add(message)
        return message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'date']