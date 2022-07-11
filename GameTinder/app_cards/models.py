from django.db import models


class Profile(models.Model):
    tg_id = models.PositiveIntegerField(
        verbose_name='ID telegram пользователя',
        unique=True,
    )
    name = models.CharField(
        max_length=256,
        verbose_name='имя пользователя',
    )

    def __str__(self):
        return f'{self.tg_id} {self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Group(models.Model):
    icon = models.ImageField()
    name = models.CharField(max_length=25)
    about = models.TextField(max_length=1500)
    players = models.ManyToManyField('Profile')


class Games(models.Model):
    icon = models.ImageField()
    name = models.CharField(max_length=256)
    players = models.ManyToManyField('Profile')

