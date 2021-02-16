from django.urls import path
from .apiviews import StudentListView, StudentDetailUpdateView, MainUserDetailView, \
                      TeacherListView, TeacherDetailView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>', StudentDetailUpdateView.as_view(), name='current_student'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>', TeacherDetailView.as_view(), name='current_teacher'),
    path('users/<int:pk>', MainUserDetailView.as_view(), name='current_user'),
]