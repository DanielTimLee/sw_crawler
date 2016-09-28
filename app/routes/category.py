from flask import jsonify, redirect, url_for, render_template

from app import app, db
from app.forms.category import CategoryForm
from app.models.category import CategoryModel


@app.route('/category')
def category():
    categories = CategoryModel.query.all()
    category_list = []
    for category in categories:
        category_list.append({
            'id': category.id,
            'name': category.name,
            'title': category.title
        })

    return jsonify({
        'item': category_list
    })


@app.route('/category/add')
def category_add():
    form = CategoryForm()

    if form.validate_on_submit():
        new_category = CategoryModel(
            name=form.name.data,
            title=form.title.data,
        )

        db.session.add(new_category)
        db.session.commit()

        return redirect(url_for('category'))

    return render_template('category_add.html', form=form)
