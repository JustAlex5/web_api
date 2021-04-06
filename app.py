from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWord(Resource):
    def get(self):
        return{"data":"Hello Developer"}

api.add_resource(HelloWord,"/helloword")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
