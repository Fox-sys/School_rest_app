from django.urls import path
from .apiviews import GroupListView, GroupUpdateDetailView, HomeworkListCreateView, \
                      HomeworkDetailView, SubjectListView, SubjectDetailView, \
                      HomeworkUpdateView

urlpatterns = [
    path('groups/', GroupListView.as_view(), name="group_list"),
    path('groups/<int:pk>', GroupUpdateDetailView.as_view(), name="current_group"),
    path('homework/', HomeworkListCreateView.as_view(), name="homework_list"),
    path('homework/<int:pk>', HomeworkDetailView.as_view(), name="current_homework"),
    path('homework/<int:pk>/update', HomeworkUpdateView.as_view(), name="update_homework"),
    path('subjects/', SubjectListView.as_view(), name="subject_list"),
    path('subjects/<int:pk>', SubjectDetailView.as_view(), name="current_subject"), 
]