from flask import jsonify, request, redirect, url_for

from app import app, db
from app.models.document import DocumentModel


@app.route('/document')
def document():
    documents = DocumentModel.query.all()
    document_list = []
    for document in documents:
        document_list.append({
            'id': document.id,
            'username': document.name,
            'title': document.title,
            'content': document.content,
            'category': document.category
        })

    return jsonify({
        'item': document_list
    })


@app.route('/document/add')
def document_add():
    # TODO: 폼 생성 + 뷰 구현 + request 처리.
    new_document = DocumentModel(
        username=request,
        title=request.remote_addr,
        content=request.document,
    )

    db.session.add(new_document)
    db.session.commit()

    return redirect(url_for('document'))
