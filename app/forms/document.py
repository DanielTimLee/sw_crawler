from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class DocumentForm(FlaskForm):
    username = StringField('Username', [
        validators.DataRequired(message='사용자 이름은 반드시 입력해주세요.'),
    ])
    content = TextAreaField('Contents', [
        validators.DataRequired(message=u'글 내용은 반드시 입력해주세요.')
    ])
