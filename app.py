from flask import Flask
from flask_restx import Api, Resource
import dotenv
app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {"hello": ["world!","bi"],"number":12}

if __name__ == '__main__':
    # debug를 True로 세팅하면, 해당 서버 세팅 후에 코드가 바뀌어도 문제없이 실행됨. 
    app.run(host='0.0.0.0', port=8000, debug = True)

