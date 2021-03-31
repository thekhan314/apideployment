from flask import Flask
from flask_restful import Resource, Api




app = Flask(__name__)
api =  Api(app)

records = {
    "cat":"mammal",
    "parrot":"bird",
    "lizard":"reptile"
}
class Creature(Resource):
    def get(self, name):
        return records[name]

api.add_resource(Creature, '/creature/<string:name>')

app.run()
