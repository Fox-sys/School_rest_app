from rest_framework.permissions import BasePermission
from .models import Message, Chat

class CanUseMessage(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.check_user_permissions(request.user)
    

class UserIsInChat(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.check_user_permissions(request.user)