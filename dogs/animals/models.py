from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class AnimalOne(models.Model):
    nickname = models.CharField(max_length=20, help_text="Не более 20 символов", unique=True, verbose_name="Кличка")
    age = models.CharField(max_length=30, help_text="не более 30 симоволов", blank=True, verbose_name="возраст")
    description = models.TextField(max_length=200, help_text="не более 200 символов", verbose_name='Описание')
    date = models.DateField(help_text='Дата появления в приюте', blank=True, verbose_name='Дата появления в приюте')
    email = models.EmailField(verbose_name="электронная почта для связи", blank=True)
    comment = models.TextField(verbose_name="контактная информация", blank=False, max_length=200)
    status = models.BooleanField(null=True, default=True, help_text="Ищет ли дом сейчас", verbose_name="Ищет дом")
    shelter = models.ForeignKey('Shelter', null=True, on_delete=models.PROTECT, verbose_name='Приют')
    cover = models.ImageField(upload_to=user_directory_path, verbose_name='Основное изображение', null=True)
    photos = models.ImageField(upload_to=user_directory_path, null=True)
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["nickname"]
        verbose_name = "Животное"
        verbose_name_plural = "Животные"

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.nickname

class Shelter(models.Model):
    name = models.CharField(max_length=20, help_text="Не более 20 символов", unique=True, verbose_name='Название приюта')
    description = models.TextField(max_length=200, help_text="не более 200 символов", verbose_name="Описание и контакты")
    email = models.EmailField(verbose_name="электронная почта для связи", blank=True)
    link = models.URLField(verbose_name="Ссылка", blank='True')

    class Meta:
        ordering = ["name"]
        verbose_name = "Приют"
        verbose_name_plural = "Приюты"

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name
