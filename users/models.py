from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser


# Create your models here.

class SiteUser(AbstractUser):
    is_consultant = models.BooleanField(default=False, verbose_name='Регистрируюсь как диетолог')



class ProfileConsultant(models.Model):
    user = models.OneToOneField(SiteUser, on_delete=models.CASCADE)
    firstname = models.TextField(verbose_name="Имя", max_length=200, null=True)
    lastname = models.TextField(verbose_name="Фамилия", max_length=200, null=True)
    surname = models.TextField(verbose_name="Отчество", max_length=200, null=True)
    education = models.TextField(verbose_name="Образование", max_length=500, null=True)
    experience = models.IntegerField(verbose_name="Опыт", null=True)
    is_activate = models.BooleanField(verbose_name="Профиль активирован", null=True)
    description = models.TextField(verbose_name="Описание", max_length=500, null=True)
    image = models.ImageField(verbose_name="Изображение профиля",  default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile Consultant'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class ProfileUser(models.Model):
    SEX_CHOICES =(
    ("M", "Мужской"),
    ("F", "Женский"),
    )
    user = models.OneToOneField(SiteUser, on_delete=models.CASCADE)
    firstname = models.TextField(verbose_name="Имя", max_length=200, null=True)
    lastname = models.TextField(verbose_name="Фамилия", max_length=200, null=True)
    surname = models.TextField(verbose_name="Отчество", max_length=200, null=True)
    sex = models.TextField(verbose_name="Пол", max_length=1, null=True, choices=SEX_CHOICES)
    bday = models.DateField(verbose_name="Дата рождения", default='1990-01-01')
    height = models.IntegerField(verbose_name="Рост (см)", default=0)
    weight = models.FloatField(verbose_name="Вес (кг)", default=0)
    image = models.ImageField(verbose_name="Изображение профиля",  default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile User'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)