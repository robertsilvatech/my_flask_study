from db import db

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    status = db.Column(db.Integer)

    def __init__(self, name, last_name, email, password, status=1):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'status': self.status
        }

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.get_or_404(user_id)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()




