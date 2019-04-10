from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import create_app
from config import Config
from app.db import db
from app.models.person import Person
from app.models.address import Address

app = create_app(Config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()