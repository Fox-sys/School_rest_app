from rest_framework import generics
from .models import MainUser, Teacher, Student
from diary_service.models import Group
from .serializers import MainUserSerializer, StudentSerializer, TeacherSerializer
from rest_framework.serializers import ValidationError
from django.shortcuts import get_object_or_404

class StudentListView(generics.ListAPIView):
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        if len(params) <= 1:
            students = Student.objects.all()
            params = self.request.query_params
            group = params.get('group', None)
            if group:
                group = get_object_or_404(Group, pk=group)
                students = Group.students.all()
                return students
            return students
        raise ValidationError('Передано слишком много аргументов в url')
    

class StudentDetailView(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class MainUserDetailView(generics.RetrieveAPIView):
    serializer_class = MainUserSerializer
    queryset = MainUser.objects.all()


class TeacherListView(generics.ListAPIView):
    serializer_class = TeacherSerializer
    
    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            teachers = Teacher.objects.all()
            is_group_curator = params.get('is_group_curator', None)
            is_chat_curator = params.get('is_chat_curator', None)
            if group:
                return teachers.filter(is_group_curator=is_group_curator)
            if is_chat_curator:
                return teachers.filter(is_chat_curator=is_chat_curator)
            return teachers
        raise ValidationError('Передано слишком много аргументов в url')


class TeacherDetailView(generics.RetrieveAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()