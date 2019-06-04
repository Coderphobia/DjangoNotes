# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
settings.configure()

def test1_create_template():
    t = template.Template('My name is {{name}}.')
    c = template.Context({'name': 'qigaoqiang'})
    print t.render(c)


if __name__ == '__main__':
    test1_create_template()