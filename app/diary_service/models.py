from django.db import models

class Subject(models.Model):
    teacher = models.ManyToManyField('profile_service.Teacher', blank=True)
    name = models.CharField('Название', max_length=150)
    description = models.TextField('описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Group(models.Model):
    name = models.CharField('Название', max_length=150)
    students = models.ManyToManyField('profile_service.Student', blank=True, related_name='+')
    curator = models.ForeignKey('profile_service.Teacher', null=True, blank=True, on_delete=models.SET_NULL)
    subjects = models.ManyToManyField('diary_service.Subject')
    homework = models.ManyToManyField("Homework", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Homework(models.Model):
    SCORES = (
        ("1", "10"),
        ("2", "20"),
        ("3", "30"),
        ("4", "40"),
    )
    short_desc = models.CharField("Краткое описание", max_length=150)
    full_desc = models.TextField("Описание", blank=True)
    teacher = models.ForeignKey('profile_service.Teacher', null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateField('Дата начала', auto_now=True)
    end_date = models.DateField("Дата сдачи")
    pins = models.FileField("Прикреплённый документ", upload_to="homework/")
    score = models.CharField(choices=SCORES, max_length=1)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject}: {self.short_desc}"

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'