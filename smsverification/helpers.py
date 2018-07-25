# -*- coding: utf-8 -*-

"""WebHelpers used in smsverification."""

#from webhelpers import date, feedgenerator, html, number, misc, text
from markupsafe import Markup

def bold(text):
    return Markup('<strong>%s</strong>' % text)