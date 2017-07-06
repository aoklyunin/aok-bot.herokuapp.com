# -*- coding: utf-8 -*-

from django.shortcuts import render


# главная страница
def index(request):
    c = {
        'pageTitleHeader': 'Главная',
    }
    return render(request, "plan/index.html", c)


