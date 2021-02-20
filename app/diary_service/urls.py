from django.urls import path
from .apiviews import GroupListView, GroupUpdateDetailView, HomeworkListView, \
                      HomeworkDetailView, SubjectListView, SubjectDetailView, \
                      HomeworkUpdateView, HomeworkCreateView, HomeworkDestroyView

urlpatterns = [
    path('groups/', GroupListView.as_view(), name="group_list"),
    path('groups/<int:pk>', GroupUpdateDetailView.as_view(), name="current_group"),
    path('homework/', HomeworkListView.as_view(), name="homework_list"),
    path('homework/create', HomeworkCreateView.as_view(), name="homework_create"),
    path('homework/<int:pk>', HomeworkDetailView.as_view(), name="current_homework"),
    path('homework/<int:pk>/update', HomeworkUpdateView.as_view(), name="update_homework"),
    path('homework/<int:pk>/destroy', HomeworkDestroyView.as_view(), name="destroy_homework"),
    path('subjects/', SubjectListView.as_view(), name="subject_list"),
    path('subjects/<int:pk>', SubjectDetailView.as_view(), name="current_subject"), 
]