from flask import jsonify, redirect, url_for, render_template

from app import app, db
from app.forms.document import DocumentForm
from app.models.document import DocumentModel


@app.route('/document')
def document():
    documents = DocumentModel.query.all()
    document_list = []
    for document in documents:
        document_list.append({
            'id': document.id,
            'username': document.username,
            'content': document.content,
            'category': [x for x in str(document.category).split() if len(str(document.category)) > 0]
        })

    return jsonify({
        'item': document_list
    })


@app.route('/document/add', methods=['GET', 'POST'])
def document_add():
    form = DocumentForm()

    if form.validate_on_submit():
        new_document = DocumentModel(
            username=form.username.data,
            content=form.content.data,
        )

        db.session.add(new_document)
        db.session.commit()

        return redirect(url_for('document_add'))

    return render_template('document_add.html', form=form)
