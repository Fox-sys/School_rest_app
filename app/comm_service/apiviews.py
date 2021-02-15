from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ValidationError

class ChatListView(generics.ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            chats = Chat.objects.all()
            name = params.get('name', None)
            user = params.get('user', None)
            if name:
                chats = chats.filter(name__icontains=name.replace('_', ' '))
            elif user:
                chats = chats.filter(members__in=user)
            return chats
        raise ValidationError('Передано слишком много аргументов в url')
        
        
class ChatDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            messages = Message.objects.all()
            chat = params.get('chat', None)
            replies_to = params.get('replies_to', None)
            if chat:
                chat = get_object_or_404(Chat, pk=chat)
                messages = chat.messages.all()
            elif replies_to:
                messages = messages.filter(replies_to=replies_to)
            return messages
        raise ValidationError('Передано слишком много аргументов в url')


class MesssageDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()