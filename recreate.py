from flask import Flask
from models import db, Recommendation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(app)

def recreate_recommendation_table():
    with app.app_context():
        # Drop all tables
        db.drop_all()
        # Create all tables based on the models
        db.create_all()

        # Now add the new column to the 'product' table
        from sqlalchemy import text
        with db.engine.connect() as connection:
            try:
                sql_command = text("ALTER TABLE product ADD COLUMN image_url VARCHAR(255)")
                connection.execute(sql_command)
                print("Column 'image_url' added successfully!")
            except Exception as e:
                print("Error occurred:", e)

if __name__ == '__main__':
    recreate_recommendation_table()
    print("Database schema updated successfully.")
