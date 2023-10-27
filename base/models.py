from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    complete = models.BooleanField(default=False, verbose_name='Выполнено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['complete']
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
