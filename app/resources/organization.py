from flask_restful import Resource, reqparse
from models.organization import OrganizationModel

class Organization(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('status', type=int, required=False, help='status for organization')

    def post(self, name):
        data = Organization.parser.parse_args()
        org = OrganizationModel.find_by_name(name)
        if org:
            return {"message": "A org that name already exists"}, 400

        org = OrganizationModel(name=name)
        org.save_to_db()

        return {'message': 'Organization created'}

    def delete(self, name):
        org = OrganizationModel.find_by_name(name)
        if org:
            org.delete_to_db()

        return {'message': 'Organization deleted'}





class OrganizationList(Resource):
    def get(self):
        return {'organizations': [org.json() for org in OrganizationModel.query.all()]}


