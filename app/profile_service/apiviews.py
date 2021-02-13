from rest_framework import generics
from .models import MainUser, Teacher, Student
from diary_service.models import Group
from .serializers import MainUserSerializer, StudentSerializer, TeacherSerializer


class StudentListView(generics.ListAPIView):
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        students = Student.objects.all()
        params = self.request.query_params
        group = params.get('group', None)
        if group:
            group = Group.objects.get(id=group)
            students = Group.students.all()
            return students
        return students


class StudentDetailView(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class MainUserDetailView(generics.RetrieveAPIView):
    serializer_class = MainUserSerializer
    queryset = MainUser.objects.all()


class TeacherListView(generics.ListAPIView):
    serializer_class = TeacherSerializer
    
    def get_queryset(self):
        teachers = Teacher.objects.all()
        params = self.request.query_params
        group = params.get('group', None)
        chat = params.get('chat', None)
        if group:
            return teachers.filter(curated_group=group)
        if chat:
            return teachers.filter(curated_chat=chat)
        return teachers


class TeacherDetailView(generics.RetrieveAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()