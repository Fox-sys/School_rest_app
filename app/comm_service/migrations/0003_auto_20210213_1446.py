# Generated by Django 3.1.6 on 2021-02-13 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comm_service', '0002_auto_20210210_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pins',
            field=models.FileField(blank=True, null=True, upload_to='Message_files/', verbose_name='файл'),
        ),
        migrations.AlterField(
            model_name='message',
            name='replays_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comm_service.message'),
        ),
    ]