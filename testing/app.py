from flask import Flask
from flask_restful import Resource, Api
import sqlite3


app = Flask(__name__)
api =  Api(app)

class Creature(Resource):
    def get(self, name):
        connection = sqlite3.connect('animals.db')
        cursor = connection.cursor()

        get_query = "SELECT * FROM animals WHERE species=?"

        result = cursor.execute(get_query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'animal':{'name':row[1], 'category':row[2]}}
        else:
            return "no such animal!"



api.add_resource(Creature, '/creature/<string:name>')

app.run()
