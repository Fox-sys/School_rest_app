from django.db import models

class StatElement(models.Model):
    ELEMENTS = (
        ("1", "ОТ"),
        ("2", "УП"),
        ("3", "ОП"),
        ("4", "2"),
        ("5", "3"),
        ("6", "4"),
        ("7", "5"),
    )
    SCORES = (
        ("1", "10"),
        ("2", "20"),
        ("3", "30"),
        ("4", "40"),
    )
    element = models.CharField(choices=ELEMENTS, max_length=2)
    score = models.CharField(choices=SCORES, max_length=1, blank=True)
    subject = models.ForeignKey("diary_service.Subject", on_delete=models.CASCADE)
    student = models.ForeignKey("profile_service.Student", on_delete=models.CASCADE)
    teacher = models.ForeignKey('profile_service.Teacher', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.student}: ({self.get_element_display()} {self.get_score_display()}) {self.subject}"

    class Meta:
        verbose_name = 'Элемент статистики'
        verbose_name_plural = 'Элементы статистики'