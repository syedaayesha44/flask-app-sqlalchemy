from app import app, db, Product

def add_initial_products():
    products = [
        {
            "name": "Laptop",
            "description": "A powerful laptop",
            "category": "Electronics",
            "price": 999.99,
            "image_url": "https://images.fonearena.com/blog/wp-content/uploads/2020/01/Falkon-Aerbook-MarQ-Flipkart-laptop.jpg"
        },
        {
            "name": "Smartphone",
            "description": "A high-end smartphone",
            "category": "Electronics",
            "price": 799.99,
            "image_url": "https://rukminim2.flixcart.com/image/850/1000/xif0q/mobile/m/e/8/-original-imagbwx4mqamdbzj.jpeg?q=90"
        },
        {
            "name": "Headphones",
            "description": "Noise-cancelling headphones",
            "category": "Electronics",
            "price": 199.99,
            "image_url": "https://rukminim1.flixcart.com/image/832/832/keq058w0-0/headphone/0/b/d/103-wireless-boat-original-imafvccxgjypzgew.jpeg?q=70"
        }
    ]
    
    for product in products:
        new_product = Product(
            name=product['name'],
            description=product['description'],
            category=product['category'],
            price=product['price'],
            image_url=product['image_url']
        )
        db.session.add(new_product)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_initial_products()
