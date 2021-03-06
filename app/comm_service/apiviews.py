from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer, MessageUpdateSerializer, \
                         MessageCreateSerializer
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ValidationError
from .permissions import CanUseMessage, UserIsInChat

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
        
        
class ChatDetailView(generics.RetrieveAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    permission_classes = [UserIsInChat]


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

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


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class MesssageDeleteView(generics.DestroyAPIView):
    serializer_class = MessageUpdateSerializer
    queryset = Message.objects.all()
    permission_classes = [CanUseMessage]


class MesssageUpdateView(generics.UpdateAPIView):
    serializer_class = MessageUpdateSerializer
    queryset = Message.objects.all()
    permission_classes = [CanUseMessage]


class MessageDetailView(generics.RetrieveAPIView):
    serializer_class = MessageUpdateSerializer
    queryset = Message.objects.all()
    permission_classes = [UserIsInChat]