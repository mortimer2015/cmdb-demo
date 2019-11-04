# -*- coding: UTF-8 -*-
__author__ = 'hunter'

from app import db


class Asset(db.Model):
    __tablename__ = 'asset'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    disk_size = db.Column(db.String(64))
    cpu = db.Column(db.Integer)
    # users = db.relationship('User', backref='role', lazy='dynamic')

    @classmethod
    def list(cls):
        ret = cls.query.all()
        return ret

    def __repr__(self):
        return '<Disk %r>' % self.name

