from run import app
from app.db import db
from app.models.address import Address
from app.models.person import Person


with app.app_context():
    email1 = 'teste3@teste'
    owner = Person.find_by_name('Paulo')
    address = Address(email=email1, owner=owner)
    db.session.add(address)
    db.session.commit()