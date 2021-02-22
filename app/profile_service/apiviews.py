from rest_framework import generics, status
from rest_framework.response import Response
from .models import MainUser, Teacher, Student
from diary_service.models import Group
from .serializers import MainUserSerializer, StudentSerializer, TeacherSerializer
from rest_framework.serializers import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .permissions import IsATeacher, IsAccountOwner

class StudentListView(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsATeacher]
    
    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            students = Student.objects.all()
            group = params.get('group', None)
            if group:
                group = get_object_or_404(Group, pk=group)
                students = Group.students.all()
                return students
            return students
        raise ValidationError('Передано слишком много аргументов в url')
    

class StudentDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsATeacher, IsAccountOwner]

    def check_object_permissions(self, request, obj):
        for permission in self.get_permissions():
            if permission.has_object_permission(request, self, obj):
                return None
        self.permission_denied(
            request,
            message=getattr(permission, 'message', None),
            code=getattr(permission, 'code', None)
        )


class MainUserDetailView(generics.RetrieveAPIView):
    serializer_class = MainUserSerializer
    queryset = MainUser.objects.all()
    permission_classes = [IsATeacher, IsAccountOwner]

    def check_object_permissions(self, request, obj):
        for permission in self.get_permissions():
            if permission.has_object_permission(request, self, obj):
                return None
        self.permission_denied(
            request,
            message=getattr(permission, 'message', None),
            code=getattr(permission, 'code', None)
        )

class TeacherListView(generics.ListAPIView):
    serializer_class = TeacherSerializer
    
    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            teachers = Teacher.objects.all()
            is_group_curator = params.get('is_group_curator', None)
            is_chat_curator = params.get('is_chat_curator', None)
            if group:
                return teachers.filter(is_group_curator=bool(is_group_curator))
            if is_chat_curator:
                return teachers.filter(is_chat_curator=bool(is_chat_curator))
            return teachers
        raise ValidationError('Передано слишком много аргументов в url')


class TeacherDetailView(generics.RetrieveAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class Logout(APIView):
    def get(self, request, format=None):
        get_object_or_404(Token, user=request.user).delete()
        return Response(status=status.HTTP_200_OK)