from django.contrib import admin
from .models import Subject, Group, Homework

admin.site.register(Homework)
admin.site.register(Group)
admin.site.register(Subject)

