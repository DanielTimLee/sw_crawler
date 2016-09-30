from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField

from app.models.category import CategoryModel


# TODO : 이런식으로 호출하면, 체크박스간의 거리가 좁아 보기가 불편할 수도 있음.
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class ClassifyForm(FlaskForm):
    category = CategoryModel.query.all()
    choice = [(x.name, x.title) for x in category]
    classify = MultiCheckboxField('classify', choices=choice)
