from django.urls import path
from .apiviews import NewsCreateView, NewsDetailView, NewsListView, \
                      NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='current_news'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='news_delete'),
    path('create', NewsCreateView.as_view(), name='news_create'),
]