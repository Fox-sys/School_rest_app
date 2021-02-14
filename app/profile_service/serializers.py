from rest_framework import serializers
from .models import MainUser, Teacher, Student


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['id', 'username', 'last_name', 'first_name', 'middle_name', \
                  'email', 'phone', 'chats', 'is_staff', 'is_active']
        
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'group', 'stats']
        

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'is_group_curator', 'is_chat_curator', \
                  'curated_group', 'curated_chat', 'photo', 'info', 'subjects']

        
