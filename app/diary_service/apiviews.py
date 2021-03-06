from rest_framework import generics
from .models import Subject, Group, Homework
from .serializers import SubjectSerializer, GroupSerializer, HomeworkSerializer, \
    HomeworkUpdateSerializer, HomeworkCreateSerializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .permissions import UserIsInGroup
from profile_service.permissions import IsATeacher


class GroupListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            groups = Group.objects.all()
            subject = params.get('subject', None)
            if subject:
                groups = groups.filter(subjects__in=subject)
            return groups
        raise ValidationError('Передано слишком много аргументов в url')


class GroupUpdateDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsATeacher]


class HomeworkListView(generics.ListAPIView):
    permission_classes = [UserIsInGroup, IsATeacher]
    serializer_class = HomeworkSerializer

    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            homework = Homework.objects.all()
            teacher = params.get('teacher', None)
            start_date = params.get('start_date', None)
            end_date = params.get('end_date', None)
            group = params.get('group', None)
            if teacher:
                homework = homework.filter(teacher=teacher)
            elif start_date:
                homework = homework.filter(start_date=start_date)
            elif end_date:
                homework = homework.filter(end_date=end_date)
            elif group:
                group = get_object_or_404(Group, pk=group)
                homework = group.homework.all()
            return homework
        raise ValidationError('Передано слишком много аргументов в url')

    def check_object_permissions(self, request, obj):
        for permission in self.get_permissions():
            if permission.has_object_permission(request, self, obj):
                return None
        self.permission_denied(
            request,
            message=getattr(permission, 'message', None),
            code=getattr(permission, 'code', None)
        )


class HomeworkCreateView(generics.CreateAPIView):
    serializer_class = HomeworkCreateSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsATeacher]


class HomeworkDetailView(generics.RetrieveAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsATeacher, UserIsInGroup]

    def check_object_permissions(self, request, obj):
        for permission in self.get_permissions():
            if permission.has_object_permission(request, self, obj):
                return None
        self.permission_denied(
            request,
            message=getattr(permission, 'message', None),
            code=getattr(permission, 'code', None)
        )


class HomeworkDestroyView(generics.DestroyAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsATeacher]


class HomeworkUpdateView(generics.UpdateAPIView):
    serializer_class = HomeworkUpdateSerializer
    queryset = Homework.objects.all()
    permission_classes = [IsATeacher]


class SubjectListView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            subjects = Subject.objects.all()
            teacher = params.get('teacher', None)
            group = params.get('group', None)
            if teacher:
                subjects = subjects.filter(teacher__in=teacher)
            elif group:
                group = get_object_or_404(Group, pk=group)
                subjects = group.subject.all()
            return subjects
        raise ValidationError('Передано слишком много аргументов в url')


class SubjectDetailView(generics.RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
