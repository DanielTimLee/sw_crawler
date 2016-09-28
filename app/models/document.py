import datetime

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import LONGTEXT, TIMESTAMP, INTEGER, SET

from app import db


class DocumentModel(db.Model):
    __tablename__ = 'documents'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    category_enum = ('Null', 'family', 'business', 'shopping', 'sports',
                     'food', 'entertain', 'hobby', 'tech', 'health')

    id = Column(
        INTEGER(20, unsigned=True),
        primary_key=True
    )
    username = Column(
        String(80),
        nullable=False
    )
    content = db.Column(
        LONGTEXT,
        nullable=False
    )
    category = db.Column(
        SET(*category_enum)
    )
    created_date = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow()
    )
