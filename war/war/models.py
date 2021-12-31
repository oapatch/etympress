# Copyright 2021 Orchid Ber. All Rights Reserved.

from django.db import models
from django.utils import timezone


class Weekday(models.IntegerChoices):
    MON = 1
    TUES = 2
    WEDNES = 3
    THURS = 4
    FRI = 5
    SATUR = 6
    SUN = 7

    @staticmethod
    def today():
        return timezone.now().weekday() + 1


class Repetition(models.IntegerChoices):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5

    @staticmethod
    def today():
        timezone_now = timezone.now()
        day = timezone_now.day
        weekday = timezone_now.weekday() + 1
        rep = 1
        day_counter = day
        while(day_counter > 7):
            day_counter = day_counter - 7
            rep = rep + 1
        return rep


class Month(models.IntegerChoices):
    JULY = 1
    AUGUST = 2
    SEPTEM = 3
    OCTO = 4
    NOVEM = 5
    DECEM = 6
    JANU = 7
    FEBRU = 8
    MARCH = 9
    APRIL = 10
    MAY = 11
    JUNE = 12

    @staticmethod
    def today():
        shifted = (timezone.now().month + 6) % 12
        if shifted == 0:
            return 12
        else:
            return shifted


