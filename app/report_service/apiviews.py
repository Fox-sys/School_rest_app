from rest_framework import generics
from .models import StatElement
from .serializers import StatElementSerializer, StatElementUpdateCreateSerializer

class StatElementListView(generics.ListAPIView):
    queryset = StatElement.objects.all()
    serializer_class = StatElementSerializer


class StatElementDetailDeleteView(generics.RetrieveDestroyAPIView):
    queryset = StatElement.objects.all()
    serializer_class = StatElementSerializer


class StatElementCreateView(generics.CreateAPIView):
    queryset = StatElement.objects.all()
    serializer_class = StatElementUpdateCreateSerializer


class StatElementUpdateView(generics.UpdateAPIView):
    queryset = StatElement.objects.all()
    serializer_class = StatElementUpdateCreateSerializer