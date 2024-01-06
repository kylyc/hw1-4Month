from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Запросы на связи"
        verbose_name_plural = "Запросы на связь"


class Reserv(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    date  = models.CharField(
        max_length=255,
        verbose_name= "Дата"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    class Meta:
        verbose_name = 'Брони'
        verbose_name_plural = "Бронь"