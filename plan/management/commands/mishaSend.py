# coding=utf-8
# программа для загрузки оценок
import datetime

import itertools
from django.contrib.auth.models import User
from django.core.management import BaseCommand

# описание класса програмы
from localCode.VKHelper import VKHelper


class Command(BaseCommand):
    # описание программы
    helf = 'mishaSend'

    def getWord(self, a):
        if a != 11 and a != 12 and a != 13 and a != 13 and a != 14:
            if a % 10 == 1:
                return "день"
            elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
                return "дня"
        return "дней"

    def getDays(self):
        a = '2017-08-20'.split('-')
        aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
        bb = datetime.date.today()
        s = str(aa - bb).split()[0]
        return s + " " + self.getWord(int(s))

    def add_arguments(self, parser):
        parser.add_argument('pass', nargs='+', type=str)

    def handle(self, *args, **options):
        vkh = VKHelper(options['pass'][1])
        vkh.sendMessageWithPicture("Осталось хуй да нихуя: "+self.getDays()+".", VKHelper.MISHA_ID,'photo303154598_456239452')

