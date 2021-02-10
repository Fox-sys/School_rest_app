from django.db import models

class News(models.Model):
    TYPES = (
        ('rp', 'Замена'),
        ('nw', 'Новость'),
        ('an', 'Объявление'),
    )
    news_type = models.CharField("Тип", choices=TYPES, max_length=2)
    title = models.CharField("Название", max_length=150)
    info = models.TextField("Текст")
    subject_from = models.ForeignKey("diary_service.Subject", on_delete=models.CASCADE, blank=True, related_name='+')
    subject_to = models.ForeignKey("diary_service.Subject", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.get_news_type_display()}: {self.title}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"