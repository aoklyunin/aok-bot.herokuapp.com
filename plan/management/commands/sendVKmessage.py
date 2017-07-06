# coding=utf-8
# программа для загрузки оценок
import datetime

import itertools
from django.contrib.auth.models import User
from django.core.management import BaseCommand


# описание класса програмы
class Command(BaseCommand):
    # описание программы
    helf = 'sendVKmessage'

    def handle(self, *args, **options):
        print("yep")
