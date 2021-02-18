from rest_framework.permissions import BasePermission
from .models import Message, Chat

class CanUseMessage(BasePermission):
    def has_object_permission(self, request, view, obj):
        chat = Chat.objects.get(messages=obj.id)
        return request.user in chat.members.all()
    

class UserIsInChat(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.members.all()