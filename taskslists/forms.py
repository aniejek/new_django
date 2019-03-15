from django.forms import ModelForm
from django import forms

from .models import TasksList, Task


class TasksListForm(ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = TasksList
        exclude = ('owner', 'creation_date')


class TaskForm(ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Task
        exclude = ('tasks_list', 'done')
