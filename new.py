from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()

# Define your Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(app)

# Rest of your code goes here...

metadata = MetaData()
metadata.reflect(bind=db.engine)

for table in metadata.tables.values():
    print(table)
