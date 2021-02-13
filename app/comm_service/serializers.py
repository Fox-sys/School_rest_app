from rest_framework import serializers
from .models import Chat, Message

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["name", "members", 'curator', 'is_curated', 'messages']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["author", "replays_to", 'text', 'pins', 'date', 'is_edited']