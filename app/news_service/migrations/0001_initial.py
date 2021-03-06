# Generated by Django 3.1.6 on 2021-02-10 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diary_service', '0002_auto_20210210_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_type', models.CharField(choices=[('rp', 'Замена'), ('nw', 'Новость'), ('an', 'Объявление')], max_length=2, verbose_name='Тип')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('info', models.TextField(verbose_name='Текст')),
                ('subject_from', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='diary_service.subject')),
                ('subject_to', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='diary_service.subject')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
