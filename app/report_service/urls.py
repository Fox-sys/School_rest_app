from django.urls import path
from .apiviews import StatElementCreateView, StatElementDetailDeleteView, StatElementListView, \
                      StatElementUpdateView

urlpatterns = [
    path('', StatElementListView.as_view(), name='stat_element_list'),
    path('<int:pk>/', StatElementDetailDeleteView.as_view(), name='current_stat_element'),
    path('<int:pk>/update/', StatElementUpdateView.as_view(), name='stat_element_update'),
    path('create', StatElementCreateView.as_view(), name='stat_element_create'),
]