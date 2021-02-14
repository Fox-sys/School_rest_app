from django.urls import path
from .apiviews import NewsCreateView, NewsDetailDeleteView, NewsListView, NewsUpdateView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailDeleteView.as_view(), name='current_news'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='news_update'),
    path('create', NewsCreateView.as_view(), name='news_create'),
]