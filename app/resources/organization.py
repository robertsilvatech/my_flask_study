from flask_restful import Resource, reqparse
from models.organization import OrganizationModel

class Organization(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='email is missing organization')
    parser.add_argument('status', type=int, required=False, help='status is missing organization')
    
    def get(self, org_id):
        print('ID {}'.format(org_id))
        org = OrganizationModel.find_by_id(org_id)
        return {'result': org.json()}
        

    def post(self, org_id):
        data = Organization.parser.parse_args()
        org = OrganizationModel.find_by_id(org_id)
        if org:
            return {"message": "A org that name already exists"}, 400

        org = OrganizationModel(name, **data)
        org.save_to_db()

        return {'message': 'Organization created'}, 201

    def delete(self, org_id):
        org = OrganizationModel.find_by_id(org_id)
        if org:
            org.delete_to_db()

        return {'message': 'Organization deleted'}

    def put(self, org_id):
        data = Organization.parser.parse_args()
        org = OrganizationModel.find_by_id(org_id)
        if org is None:
            org = OrganizationModel(name, **data)
            return {'message': 'Organization created',
                'result': org.json()}, 201
        else:
            org.email = data['email']
            org.status = data['status']
            return {'message': 'Organization edited',
            'result': org.json()}, 201
        
        org.save_to_db()

        

        

            

class OrganizationList(Resource):
    def get(self):
        return {'organizations': [org.json() for org in OrganizationModel.query.all()]}


