from flask import render_template, request
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound

from app import app, db
from app.models.category import CategoryModel
from app.models.document import DocumentModel


@app.route('/classify', methods=['GET', 'POST'])
def classify():
    try:
        categories = CategoryModel.query.all()
        document = DocumentModel.query.filter_by(category=None). \
            order_by(func.rand()).first()

    except NoResultFound:
        return "Category or Document Not Found"

    if request.method == "POST":
        selected_contacts = request.form.getlist("category")

        document.category = selected_contacts
        db.session.commit()
        print(selected_contacts)

    return render_template('classify.html', document=document, categories=categories)
