from app import app
from flask import render_template

@app.route('/<string:user>')
def index(user):
    return render_template('index.html',user=user)
