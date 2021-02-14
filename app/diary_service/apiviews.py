from rest_framework import generics
from .models import Subject, Group, Homework
from .serializers import SubjectSerializer, GroupSerializer, HomeworkSerializer, \
                         HomeworkUpdateSerializer

class GroupListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    
    def get_queryset(self):
        groups = Group.objects.all()
        params = self.request.query_params
        subject = params.get('subject', None)
        if subject:
            groups = groups.filter(subjects__in=subject)
        return groups


class GroupUpdateDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class HomeworkListCreateView(generics.ListCreateAPIView):
    serializer_class = HomeworkSerializer
    
    def get_queryset(self):
        homework = Homework.objects.all()
        params = self.request.query_params
        teacher = params.get('teacher', None)
        if teacher:
            homework = homework.filter(teacher=teacher)
        return homework


class HomeworkDetailView(generics.RetrieveAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()


class HomeworkUpdateView(generics.UpdateAPIView):
    serializer_class = HomeworkUpdateSerializer
    queryset = Homework.objects.all()


class SubjectListView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    
    def get_queryset(self):
        subjects = Subject.objects.all()
        params = self.request.query_params
        teacher = params.get('teacher', None)
        if teacher:
            subjects = subjects.filter(teacher__in=teacher)
        return subjects


class SubjectDetailView(generics.RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()