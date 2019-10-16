# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def calc(request):
    for i in range(1,40):
        print i * i
    return HttpResponse('done')
