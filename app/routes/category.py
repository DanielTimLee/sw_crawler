from flask import jsonify, request, redirect, url_for

from app import app, db
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
    # TODO: 폼 생성 + 뷰 구현 + request 처리.
    new_category = CategoryModel(
        name=request,
        title=request.remote_addr
    )

    db.session.add(new_category)
    db.session.commit()

    return redirect(url_for('category'))
