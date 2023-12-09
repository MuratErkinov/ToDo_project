from django.db import models


class ToMeet(models.Model):
    persone = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_of_meeting = models.DateTimeField()
    comment = models.TextField(null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Goal_for_month(models.Model):

    MONTH_CHOICES = [
        ("Январь", "Январь"),
        ("Февраль", "Февраль"),
        ("Март", "Март"),
        ("Апрель", "Апрель"),
        ("Май", "Май"),
        ("Июнь", "Июнь"),
        ("Июль", "Июль"),
        ("Августь", "Августь"),
        ("Сентябрь", "Сентябрь"),
        ("Октябрь", "Октябрь"),
        ("Ноябрь", "Ноябрь"),
        ("Декабрь", "Декабрь")
    ]

    goal = models.CharField(max_length=250)
    month = models.CharField(max_length=10, choices=MONTH_CHOICES, default="Январь")
    difficulty = models.PositiveSmallIntegerField()
    reason_for_goal = models.TextField()
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Habits(models.Model):
    name = models.CharField(max_length=40)
    comment = models.TextField()
    done_for_today = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
