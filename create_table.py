# create_table.py

from flask import Flask
from models import db
from sqlalchemy import create_engine  # Import create_engine from SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(app)

def create_recommendation_table():
    with app.app_context():
        # Create all tables in the database
        db.create_all()

from sqlalchemy import text

def create_purchase_table():
    engine = create_engine('sqlite:///ecommerce.db')  # Adjust the database URI as needed
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS purchase (
                user_id INTEGER,
                product_id INTEGER,
                PRIMARY KEY (user_id, product_id),
                FOREIGN KEY (user_id) REFERENCES user (id),
                FOREIGN KEY (product_id) REFERENCES product (id)
            )
        """))

if __name__ == '__main__':
    create_recommendation_table()
    print('craeted')
    create_purchase_table()
    print("Purchase table created successfully.")