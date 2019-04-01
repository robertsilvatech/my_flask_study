from flask import Flask
from flask_restful import Api
from db import db
from config import Config
from resources.check import Check
from resources.organization import Organization, OrganizationList
from resources.user import User, UserList

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

api.add_resource(Check, '/check')
api.add_resource(User, '/user/<string:name>')
api.add_resource(UserList, '/users')
api.add_resource(Organization, '/org/<int:org_id>')
api.add_resource(OrganizationList, '/orgs')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run()
