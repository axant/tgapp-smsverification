# -*- coding: utf-8 -*-
from sqlalchemy import ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import backref, relation
from tgext.pluggable.sqla import primary_key

from smsverification.model import DBSession, DeclarativeBase
from tgext.pluggable import app_model


class SMSVerification(DeclarativeBase):
    __tablename__ = 'smsverification_smsverification'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    phone_number = Column(Unicode(32), default=None)

    user_id = Column(Integer, ForeignKey(primary_key(app_model.User)))
    user = relation(app_model.User, uselist=False,
                    backref=backref('smsverification', uselist=False, cascade='all'))
