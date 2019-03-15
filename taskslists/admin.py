# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import TasksList, Task


@admin.register(TasksList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'creation_date')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tasks_list')

