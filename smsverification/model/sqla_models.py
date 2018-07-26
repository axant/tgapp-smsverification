# -*- coding: utf-8 -*-
from sqlalchemy import ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import backref, relation
from smsverification.model import DBSession, DeclarativeBase

from datetime import datetime


class SMSVerification(DeclarativeBase):
    __tablename__ = 'smsverification_smsverification'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now)  # il time preso da tgapp-registration
    phone_number = Column(Unicode(32), nullable=False)
    pin = Column(Integer, nullable=False)
    verified = Column(DateTime, default=None)

    user_id = Column(Integer, ForeignKey(primary_key(app_model.User)))
    user = relation(app_model.User, uselist=False,
                    backref=backref('smsverification', uselist=False, cascade='all'))
