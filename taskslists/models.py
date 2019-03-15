# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related


class TasksListsQuerySet(models.QuerySet):
    def user_tasks_lists(self, user):
        ret = self.filter(
            owner=user
        )
        return ret


class TasksList(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(User,
                              related_name="tasks_lists_owner",
                              on_delete=models.CASCADE)
    objects = TasksListsQuerySet.as_manager()

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.name == "":
            raise ValidationError("Empty task name")

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50, blank=False)
    tasks_list = models.ForeignKey(TasksList, on_delete=models.CASCADE,
                                   related_name="list_tasks")
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return cross_out(str(self.name))
        else:
            return self.name


def cross_out(string):
    ret = ""
    for char in string:
        ret += char + '\u0336'
    return ret
