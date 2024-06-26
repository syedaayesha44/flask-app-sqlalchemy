from flask import Flask
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(app)

# Define a context manager to run the script within the application context
with app.app_context():
    # Fetch all products from the database
    products = Product.query.all()

    # Print out the details of each product
    for product in products:
        print(f"Product ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Description: {product.description}")
        print(f"Category: {product.category}")
        print(f"Price: {product.price}")
        print(f"Image URL: {product.image_url}")
        print(f"Flipkart URL: {product.flipkart_url}")
        print("\n")
from flask import Flask
from models import db, Product  # Import your SQLAlchemy models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(app)

# Create the Flask app context
with app.app_context():
    # Create instances of Product model for new products
    new_products = [
        Product(name='Vacuum Cleaner', description='A powerful vacuum cleaner', category='Home Appliances', price=149.99, image_url='https://example.com/vacuum_cleaner.jpg', flipkart_url='https://www.flipkart.com/vacuum-cleaner'),
        Product(name='Jewelry', description='Beautiful jewelry pieces', category='Accessories', price=299.99, image_url='https://example.com/jewelry.jpg', flipkart_url='https://www.flipkart.com/jewelry'),
        Product(name='Coffee Pods', description='Variety of coffee pods', category='Food & Beverage', price=19.99, image_url='https://example.com/coffee_pods.jpg', flipkart_url='https://www.flipkart.com/coffee-pods'),
        Product(name='Books', description='Bestselling books', category='Books', price=39.99, image_url='https://example.com/books.jpg', flipkart_url='https://www.flipkart.com/books'),
        Product(name='Clothing', description='Stylish clothing items', category='Fashion', price=79.99, image_url='https://example.com/clothing.jpg', flipkart_url='https://www.flipkart.com/clothing'),
        # Add more Product instances for other products here
         Product(name='Wireless Earbuds', description='High-quality wireless earbuds', category='Electronics', price=89.99, image_url='https://example.com/earbuds.jpg', flipkart_url='https://www.flipkart.com/wireless-earbuds'),
        Product(name='Smartwatch', description='Feature-rich smartwatch', category='Electronics', price=199.99, image_url='https://example.com/smartwatch.jpg', flipkart_url='https://www.flipkart.com/smartwatch'),
        Product(name='Fitness Tracker', description='Track your fitness activities', category='Fitness', price=79.99, image_url='https://example.com/fitness_tracker.jpg', flipkart_url='https://www.flipkart.com/fitness-tracker'),
        Product(name='Sunglasses', description='Stylish sunglasses for any occasion', category='Accessories', price=49.99, image_url='https://example.com/sunglasses.jpg', flipkart_url='https://www.flipkart.com/sunglasses'),
        Product(name='Gaming Console', description='Next-gen gaming console', category='Gaming', price=399.99, image_url='https://example.com/gaming_console.jpg', flipkart_url='https://www.flipkart.com/gaming-console')
    ]

    # Add the new products to the session
    db.session.add_all(new_products)

    # Commit the session to save the changes to the database
    db.session.commit()

print("New products added successfully!")
