# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import defaultdict

from django.db import models
from django.contrib.auth.models import User


class HomePageVisit(models.Model):
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    who = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.start_date)
