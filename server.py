from flask import Flask

app=Flask(__name__)

@app.route('/<string:user>')
def index(user):
    return "hi " + user

app.run(debug=True,host='0.0.0.0',port=8888)
