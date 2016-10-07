from flask_wtf import FlaskForm
from wtforms import StringField, validators


class CrawlerForm(FlaskForm):
    target = StringField('target', [
        validators.DataRequired(message='크롤링할 타겟을 입력해 주세요.'),
    ])
