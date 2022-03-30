from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
# Le point d'entré de l'application, il doit être initialisé avec une application Flask
api = Api(app)


class Home(Resource):
    def get(self):
        return {'message': 'Hello World'}, 200


# Déclaration des routes
api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run()  # run our Flask app