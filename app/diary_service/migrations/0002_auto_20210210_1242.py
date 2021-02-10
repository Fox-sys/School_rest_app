# Generated by Django 3.1.6 on 2021-02-10 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_service', '0001_initial'),
        ('diary_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ManyToManyField(blank=True, to='profile_service.Teacher'),
        ),
        migrations.AddField(
            model_name='homework',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary_service.subject'),
        ),
        migrations.AddField(
            model_name='homework',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile_service.teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile_service.teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='homework',
            field=models.ManyToManyField(blank=True, to='diary_service.Homework'),
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='_group_students_+', to='profile_service.Student'),
        ),
    ]
