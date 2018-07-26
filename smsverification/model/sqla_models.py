# -*- coding: utf-8 -*-
from random import randint
from sqlalchemy import ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import backref, relation
from smsverification.model import DBSession, DeclarativeBase
from tgext.pluggable import app_model
from datetime import datetime


class SMSVerification(DeclarativeBase):
    __tablename__ = 'smsverification_smsverification'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now)
    phone_number = Column(Unicode(32), nullable=False)
    pin = Column(Unicode(5), nullable=False)
    verified = Column(DateTime, default=None)

    user_id = Column(Integer, ForeignKey(primary_key(app_model.User)))
    user = relation(app_model.User, uselist=False,
                    backref=backref('smsverification', uselist=False, cascade='all'))

    @classmethod
    def generate_pin(cls):
        pin = str()
        for i in range(0, 5):
            pin += str(randint(0, 9))
        return pin

    @classmethod
    def get_unverified(cls, number):
        return DBSession.query(SMSVerification).filter_by(verified=None)\
                    .filter_by(phone_number=number).first()
