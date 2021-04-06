from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWord(Resource):
    def get(self):
        return{"data":"Hello Tester"}

api.add_resource(HelloWord,"/helloword")


if __name__ == "__main__":
    app.run(debug=True)
