from run import app
from app.db import db
from app.models.person import Person

with app.app_context():
    name = 'Paulo'
    person = Person(name)
    db.session.add(person)
    db.session.commit()
