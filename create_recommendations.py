from flask import Flask
from models import db, Product, Recommendation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(app)

def add_recommendations():
    with app.app_context():
        products = Product.query.all()
        for product in products:
            recommendations = generate_mock_recommendations(product.id)
            for rec in recommendations:
                recommendation = Recommendation(
                    product_id=product.id, 
                    recommended_product_id=rec['id'],
                    recommended_product_name=rec['name'],
                    category=rec['category'],
                    price=rec['price'],
                    recommended_product_description=rec['description'],
                    flipkart_url=rec['flipkart_url'],
                    image_url=rec['image_url']
                )
                db.session.add(recommendation)
        db.session.commit()

def generate_mock_recommendations(product_id):
    # Mock data for recommendations
    mock_recommendations = [
        {
            'id': 1,
            'name': 'Recommended Product 1',
            'category': 'Electronics',
            'price': 199.99,
            'description': 'This is a great product for your needs.',
            'flipkart_url': 'https://www.flipkart.com/recommended-product-1',
            'image_url': 'https://via.placeholder.com/150'
        },
        {
            'id': 2,
            'name': 'Recommended Product 2',
            'category': 'Electronics',
            'price': 299.99,
            'description': 'This product is highly recommended for its features.',
            'flipkart_url': 'https://www.flipkart.com/recommended-product-2',
            'image_url': 'https://via.placeholder.com/150'
        }
    ]
    return mock_recommendations

if __name__ == '__main__':
    add_recommendations()
