from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask import json
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
   
    def post(self):
        content = request.get_json()
        appname = content.get('message')
        print(content)
        print(appname)
        return "JSON Message: " + json.dumps(request.get_json())


api.add_resource(HelloWorld, '/messages')

if __name__ == '__main__':
    app.run(host='0.0.0.0')