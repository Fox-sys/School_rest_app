from rest_framework.permissions import BasePermission
from .models import Teacher, Student, MainUser

class IsATeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return Teacher.objects.filter(user=request.user).exists()
        return False


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.check_user_permissions(request.user)
        return False

