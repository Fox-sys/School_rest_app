from django.db import models

class Chat(models.Model):
    name = models.CharField('Название', max_length=150)
    members = models.ManyToManyField('profile_service.MainUser', blank=True)
    curator = models.ForeignKey('profile_service.Teacher', blank=True, null=True, on_delete=models.SET_NULL)
    is_curated = models.BooleanField('Чат курируется?', default=True)
    messages = models.ManyToManyField('Message', blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    author = models.ForeignKey('profile_service.MainUser', on_delete=models.CASCADE)
    replays_to = models.ForeignKey('Message', on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField('Текст', max_length=2000)
    pins = models.FileField('файл', upload_to='Message_files/', blank=True, null=True)
    date = models.DateTimeField('Дата и время')
    is_edited = models.BooleanField('Редактировалось?', default=False)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'