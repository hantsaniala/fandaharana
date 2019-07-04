from django.db import models
from django.conf import settings


class Person(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True, )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name


class Public(models.Model):
    date = models.DateField()

    hour_1 = models.TimeField()
    hour_2 = models.TimeField()

    place = models.CharField(max_length=30)

    person_1 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='public_1')

    person_2 = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='public_2')

    def __str__(self):
        date = self.date.strftime('%A %d %B %Y')
        hour_1 = self.hour_1.strftime("%HH")
        hour_2 = self.hour_2.strftime("%HH")
        return f'{date} {hour_1} - {hour_2}'
