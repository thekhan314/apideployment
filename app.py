from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)

items = [
    {'JobApplication':"Google",'date':'1/1/2021'},
    {'JobApplication':"Facebook",'date':'1/1/2021'}
]
@app.route('/')
def hello():
    return render_template('form.html', items = items)


if __name__ == '__main__':
    app.run()