from rest_framework import generics
from .models import News
from .serializers import NewsSerializer, NewsUpdateCreateSerializer
from rest_framework.serializers import ValidationError


class NewsListView(generics.ListAPIView):
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        params = self.request.query_params
        if len(params) <= 1:
            news = News.objects.all()
            news_type = params.get('news_type', None)
            subject_from = params.get('subject_from', None)
            subject_to = params.get('subject_to', None)
            if news_type:
                news = news.filter(news_type=news_type)
            elif subject_from:
                news = news.filter(subject_from=subject_from)
            elif subject_to:
                news = news.filter(subject_to=subject_to)
            return news
        raise ValidationError('Передано слишком много аргументов в url')


class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsUpdateCreateSerializer
    queryset = News.objects.all()


class NewsUpdateView(generics.UpdateAPIView):
    serializer_class = NewsUpdateCreateSerializer
    queryset = News.objects.all()


class NewsDetailDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()