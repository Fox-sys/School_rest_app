from django.contrib import admin
from .models import MainUser, Teacher, Student
from django.contrib.auth.admin import UserAdmin

@admin.register(MainUser)
class MainUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'middle_name', 'phone', 'email', 'chats')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'middle_name', 'phone')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'chats')
    filter_horizontal = ('groups', 'user_permissions', 'chats')

admin.site.register(Teacher)
admin.site.register(Student)