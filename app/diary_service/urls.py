from django.urls import path
from .apiviews import GroupListView, GroupUpdateDetailView, HomeworkListView, \
                      HomeworkUpdateDetailView, SubjectListView, SubjectDetailView

urlpatterns = [
    path('groups/', GroupListView.as_view(), name="group_list"),
    path('groups/<int:pk>', GroupUpdateDetailView.as_view(), name="current_group"),
    path('homework/', HomeworkListView.as_view(), name="homework_list"),
    path('homework/<int:pk>', HomeworkUpdateDetailView.as_view(), name="current_homework"),
    path('subjects/', SubjectListView.as_view(), name="subject_list"),
    path('subjects/<int:pk>', SubjectDetailView.as_view(), name="current_subject"), 
]