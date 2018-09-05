# -*- coding: utf-8 -*-
from formencode import validators


class UniquePhoneNumberValidator(validators.UnicodeString):
    outputEncoding = None

    def validate_python(self, value, state):
        super(UniquePhoneNumberValidator, self).validate_python(value, state)
