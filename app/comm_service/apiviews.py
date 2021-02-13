from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework import generics

class ChatListView(generics.ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        chats = Chat.objects.all()
        params = self.request.query_params
        contain = params.get('contain', None)
        if contain:
            chats = chats.filter(name__icontains=contain.replace('_', ' '))
        return chats
        
class ChatDetailView(generics.RetrieveAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

