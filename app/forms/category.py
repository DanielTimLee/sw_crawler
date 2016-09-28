from flask_wtf import Form
from wtforms import StringField, validators


class CategoryForm(Form):
    name = StringField('name', [
        validators.DataRequired(message='카테고리 name을 입력해 주세요. 반드시 영어로 입력해주세요.'),
    ])
    title = StringField('title', [
        validators.DataRequired(message=u'카테고리 이름은 반드시 입력해주세요.')
    ])
