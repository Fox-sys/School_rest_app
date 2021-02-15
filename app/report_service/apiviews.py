from rest_framework import generics
from .models import StatElement
from .serializers import StatElementSerializer, StatElementUpdateCreateSerializer
from rest_framework.serializers import ValidationError


class StatElementListView(generics.ListAPIView):
    serializer_class = StatElementSerializer

    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            stats = StatElement.objects.all()
            subject = params.get('subject', None)
            element = params.get('element', None)
            score = params.get('score', None)
            teacher = params.get('teacher', None)
            student = params.get('student', None)
            if subject:
                stats = stats.filter(subject=subject)
            elif element:
                stats = stats.filter(element=element)
            elif score:
                stats = stats.filter(score=score)
            elif teacher:
                stats = stats.filter(teacher=teacher)
            elif student:
                stats = stats.filter(student=student)
            return stats
        raise ValidationError('Передано слишком много аргументов в url')


class StatElementDetailDeleteView(generics.RetrieveDestroyAPIView):
    queryset = StatElement.objects.all()
    serializer_class = StatElementSerializer


class StatElementCreateView(generics.CreateAPIView):
    queryset = StatElement.objects.all()
    serializer_class = StatElementUpdateCreateSerializer


class StatElementUpdateView(generics.UpdateAPIView):
    queryset = StatElement.objects.all()
    serializer_class = StatElementUpdateCreateSerializer