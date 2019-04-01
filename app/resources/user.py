from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('last_name', type=str, required=True, help='fullname is missing')
    parser.add_argument('email', type=str, required=True, help='email is missing')
    parser.add_argument('password', type=str, required=True, help='password is missing')
    parser.add_argument('status', type=int, required=False, default=1, help='status is missing')

    def get(self, name):
        user = UserModel.find_by_name(name)
        if user:
            return user.json()

        return {'result': 'User not found'}, 404

    def post(self, name):
        data = User.parser.parse_args()
        if UserModel.find_by_name(name):
            return {"message": "An user with name {} already exists.".format(name)}, 400  # 400 requisição ruim

        user = UserModel(name, **data)

        user.save_to_db()

        return {'message': 'User created'}, 201

    def delete(self, name):
        user = UserModel.find_by_name(name)
        if user:
            user.delete_to_db()
            return {'message': 'User deleted'}

        return {'result': 'User not found'}, 404

    def put(self, name):
        data = User.parser.parse_args()
        user = UserModel.find_by_name(name)
        if user is None:
            user = UserModel(name, **data)

        else:
            user.last_name = data['last_name']
            user.email = data['email']
            user.password = data['password']
            user.status = data['status']

        user.save_to_db()

        return user.json()

class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}

