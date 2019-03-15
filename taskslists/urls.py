"""new_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import tasks_lists, new_tasks_list, view_tasks_list, edit_tasks_list, scratch_task

urlpatterns = [
    url(r'my_lists$', tasks_lists, name="tasks_lists"),
    url(r'new_list$', new_tasks_list, name="user_new_tasks_list"),
    url(r'view/(?P<id>\d+)/$', view_tasks_list, name="view_tasks_list"),
    url(r'edit/(?P<id>\d+)/(?P<task_id>\d+)/$', edit_tasks_list, name="edit_tasks_list"),
    url(r'scratch/(?P<id>\d+)/(?P<task_id>\d+)/$', scratch_task, name="scratch_task"),
]
