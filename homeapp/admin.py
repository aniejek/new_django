# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import HomePageVisit


@admin.register(HomePageVisit)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date')
