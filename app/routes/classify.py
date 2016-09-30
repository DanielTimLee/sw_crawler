from flask import redirect
from flask import render_template
from flask import url_for
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound

from app import app, db
from app.forms.classify import ClassifyForm
from app.models.document import DocumentModel


@app.route('/classify', methods=['GET', 'POST'])
def classify():
    try:
        document = DocumentModel.query.filter_by(category=None). \
            order_by(func.rand()).first()

    except NoResultFound:
        return "Category or Document Not Found"

    form = ClassifyForm()

    if form.validate_on_submit():
        document.category = form.classify.data
        db.session.commit()
        return redirect(url_for('classify'))
    return render_template('classify.html', document=document, form=form)
