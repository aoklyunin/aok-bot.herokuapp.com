# -*- coding: utf-8 -*-
import datetime

from django.contrib.auth.models import User
from django.db import models


class HelloText(models.Model):
    text = models.TextField(max_length=100000, null=True, blank=True)
    tp = models.IntegerField(default=0)

    def __str__(self):
        return self.text +"("+str(self.tp)+")"


