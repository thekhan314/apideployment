from flask import Flask, render_template
from flask_restful import Resource, Api
from form import JobEntry

app = Flask(__name__)

items = [
    {'JobApplication':"Google",'date':'1/1/2021'},
    {'JobApplication':"Facebook",'date':'1/1/2021'}
]
@app.route('/')
def hello():
    form = JobEntry()
    return render_template('jobentry.html',form=form)

if __name__ == '__main__':
    app.run()