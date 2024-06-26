from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    flipkart_url = db.Column(db.String(255), nullable=False)

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    recommended_product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    recommended_product_name = db.Column(db.String(150), nullable=False)
    recommended_product_description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    flipkart_url = db.Column(db.String(255), nullable=False)
def get_laptop_recommendations():
    recommendations = [
        {'name': 'Laptop 1', 'description': 'Powerful laptop with high-performance specs.', 'price': 999.99, 'image_url': 'https://example.com/laptop1.jpg'},
        {'name': 'Laptop 2', 'description': 'Slim and lightweight laptop for on-the-go productivity.', 'price': 799.99, 'image_url': 'https://example.com/laptop2.jpg'},
        {'name': 'Laptop 3', 'description': 'Gaming laptop with dedicated graphics for immersive gaming experience.', 'price': 1299.99, 'image_url': 'https://example.com/laptop3.jpg'},
    ]
    return recommendations


class Image(db.Model):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    path = Column(String, nullable=False)
    flipkart_url = Column(String, nullable=False)

    def __repr__(self):
        return f"Image(id={self.id}, image_path='{self.image_path}', flipkart_url='{self.flipkart_url}')"