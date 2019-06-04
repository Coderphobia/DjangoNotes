# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template
import datetime


# Create your views here.


def helloworld(request):
    return HttpResponse("Hello World")


def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def current_time2(request):
    now = datetime.datetime.now()
    t = Template('<html><body>It is now {{current_time}}.</body></html>')
    c = Context({'current_time': now})
    html = t.render((c))
    return HttpResponse(html)

def current_time3(request):
    now = datetime.datetime.now()
    t = get_template('time.html')
    #c = Context({'current_time': now})
    c = {'current_time': now}
    html = t.render((c))
    return HttpResponse(html)

def current_time4(request):
    now = datetime.datetime.now()
    return render(request, 'time.html', {'current_time': now})

def current_time5(request):
    current_time = datetime.datetime.now()
    return render(request, 'time.html', locals())

def current_time6(request):
    current_time = datetime.datetime.now()
    return render(request, 'current_datetime.html', locals())

def baidu(request):
    return render(request, 'baidu.html')

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def hours_ahead2(request, offset):
    try:
        hours_ahead = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hours_ahead)
    return render(request, 'future_time.html', locals())

