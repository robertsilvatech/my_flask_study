from flask_restful import Resource

class Check(Resource):
    def get(self):
        return {"message": "API is alive"}