from django.db import models
from django.contrib.auth.models import AbstractUser

class MainUser(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=150)
    phone = models.CharField('Телефон', max_length=13)
    chats = models.ManyToManyField('comm_service.Chat', blank=True)
    
    def __str__(self):
        return f'{self.username}: {self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Teacher(models.Model):
    user = models.ForeignKey('MainUser', on_delete=models.CASCADE)
    is_group_curator = models.BooleanField('Классный руководитель?', default=False)
    is_chat_curator = models.BooleanField('Куратор чата?', default=False)
    curated_group = models.ForeignKey('diary_service.Group', blank=True, null=True, on_delete=models.SET_NULL)
    curated_chat = models.ForeignKey('comm_service.Chat', blank=True, null=True, on_delete=models.SET_NULL)
    photo = models.FileField('Фото', upload_to='teacher_photos/')
    info = models.TextField('Мнформация о преподователе')
    subjects = models.ManyToManyField('diary_service.Subject', related_name='+')

    def __str__(self):
        return f'{self.user.username}: {self.user.last_name} {self.user.first_name} {self.user.middle_name}'
        
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Student(models.Model):
    user = models.ForeignKey('MainUser', on_delete=models.CASCADE)
    group = models.ForeignKey('diary_service.Group', blank=True, null=True, on_delete=models.SET_NULL)
    subjects = models.ManyToManyField('diary_service.Subject')
    stats = models.ManyToManyField('report_service.StatElement', blank=True, related_name='+')

    def __str__(self):
        return f'{self.user.username}: {self.user.last_name} {self.user.first_name} {self.user.middle_name}'
        
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'