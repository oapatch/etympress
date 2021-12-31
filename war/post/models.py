# Copyright 2021 Orchid Ber. All Rights Reserved.

# TODO trans import as _
# for localization!

from django.db import models
from war.war.models import Weekday, Repetition, Month


class CW(models.Model):
    warning = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    def __str__(self):
        if self.slug:
            return slug
        return warning


class Entry(models.Model):
    """ Kinda like a mail for a multiplex mail transfer protocol over smtp-like
    interfaces idk something like that """
    modified_from = models.ForeignKey('Entry', null=True, blank=True,
            related_name='sire', on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)
    warnings = models.ManyToManyField(CW, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True)
    licence = models.CharField(max_length=50, blank=True,
            default="All Rights Reserved.")  # TODO lotta db space here
    created = models.DateField(auto_now_add=True)
    weekday = models.IntegerField(
            db_index=True,
            choices=Weekday.choices,
            default=Weekday.today,
            editable=False)
    repetition = models.IntegerField(
            db_index=True,
            choices=Repetition.choices,
            default=Repetition.today,
            editable=False)
    month = models.IntegerField(
            db_index=True,
            choices=Month.choices,
            default=Month.today,
            editable=False)
    entry = models.TextField()
    title = models.CharField(max_length=150, blank=True)
    def __str__(self):
        month = Month(self.month).label
        repetition = Repetition(self.repetition).label
        weekday = Weekday(self.weekday).label
        if self.title and self.category:
            return '#{pk}: {title} ({category})'.format(
                    category=self.category,
                    pk=self.pk,
                    title=self.title,
            )
        elif self.title:
            return '#{pk}: {title} ({month} {repetition} of {weekday})'.format(
                    month=month, 
                    repetition=repetition,
                    weekday=weekday,
                    pk=self.pk,
                    title=self.title,
            )
        return '#{pk}: {month} {repetition} of {weekday}'.format(
                month=month, repetition=repetition, weekday=weekday, pk=self.pk,
        )

