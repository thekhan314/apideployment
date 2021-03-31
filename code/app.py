from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api =  Api(app)

class Item(Resource):

    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item

    def post(self, name):
        data = request.get_json(silent=True)
        item = {'name':name,'price':data['price']}
        items.append(item)
        return item


app.run()

items = [
]
api.add_resource(Item, '/student/<string:name>')