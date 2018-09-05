# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate
from tg.i18n import ugettext as _

from smsverification import model
from smsverification.model import DBSession
from smsverification.lib.validators import UniquePhoneNumberValidator

from tw2.forms import TableForm, SingleSelectField, TextField
from tw2.core import Required


class PhoneNumberForm(TableForm):
    country_code = SingleSelectField(validator=Required)
    phone_number = TextField(validator=UniquePhoneNumberValidator(not_empty=True))


class RootController(TGController):
    @expose('kajiki:smsverification.templates.verify')
    def index(self):
        return dict(form='form')
