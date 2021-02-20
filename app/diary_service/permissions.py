from rest_framework.permissions import BasePermission
from profile_service.models import Teacher, MainUser, Student


class UserIsInGroup(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            student = Student.objects.filter(user=request.user)
            if student.exists():
                student = student[0]
                if obj in student.group.homework.all():
                    return True
        return False
