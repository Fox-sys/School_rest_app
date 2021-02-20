from rest_framework.permissions import BasePermission
from .models import Teacher

class IsATeacher(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if Teacher.objects.filter(user=request.user).exists():
                return True
        return False