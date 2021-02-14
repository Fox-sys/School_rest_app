from rest_framework import generics
from .models import News
from .serializers import NewsSerializer, NewsUpdateCreateSerializer


class NewsListView(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsUpdateCreateSerializer
    queryset = News.objects.all()


class NewsUpdateView(generics.UpdateAPIView):
    serializer_class = NewsUpdateCreateSerializer
    queryset = News.objects.all()


class NewsDetailDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()