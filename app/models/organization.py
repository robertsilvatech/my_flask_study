from db import db

class OrganizationModel(db.Model):
    __tablename__ = 'organization'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    status = db.Column(db.Integer, default=1)

    def __init__(self, name, status=1):
        self.name = name
        self.status = status

    def json(self):
        return {'name': self.name}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()