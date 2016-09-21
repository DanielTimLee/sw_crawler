from app import app
from app.models.category import CategoryModel
from flask import jsonify

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

