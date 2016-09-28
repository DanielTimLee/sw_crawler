from flask import render_template, request

from app import app
from app.models.category import CategoryModel


@app.route('/classify', methods=['GET', 'POST'])
def classify():
    result = CategoryModel.query.all()

    if request.method == "POST":
        selected_contacts = request.form.getlist("category")
        print(selected_contacts)

    return render_template('classify.html', categories=result)
