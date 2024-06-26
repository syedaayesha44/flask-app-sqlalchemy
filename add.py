from flask import Flask
from sqlalchemy import text
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

with app.app_context():
    # Use db.session.execute with the text function to run the raw SQL command to add the new column
    db.session.execute(text('ALTER TABLE product ADD COLUMN flipkart_url VARCHAR(200)'))
    db.session.commit()

    print("Column 'flipkart_url' added successfully.")
