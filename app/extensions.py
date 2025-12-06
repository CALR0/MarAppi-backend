from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initialize extensions here so they can be imported from other modules
db = SQLAlchemy()
migrate = Migrate()
