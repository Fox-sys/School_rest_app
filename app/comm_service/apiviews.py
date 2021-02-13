from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework import generics

class ChatListView(generics.ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        chats = Chat.objects.all()
        params = self.request.query_params
        contain = params.get('contain', None)
        user = params.get('user', None)
        if contain:
            chats = chats.filter(name__icontains=contain.replace('_', ' '))
        if user:
            chats = chats.filter(members__in=user)
        return chats
        
class ChatDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        messages = Message.objects.all()
        params = self.request.query_params
        chat = params.get('chat', None)
        replay = params.get('replay', None)
        if chat:
            chat = Chat.objects.get(id=chat)
            messages = chat.messages.all()
        if replay:
            messages = messages.filter(replays_to=replay)
        return messages


class MesssageDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()