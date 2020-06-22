from flask_sqlalchemy import SQLAlchemy
from website import app

db = SQLAlchemy(app)

# Models Here

# Create all database tables
db.create_all()