from flask import Flask
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/add-sample-data')
def add_sample_data():
    sample_products = [
        Product(name='Laptop', description='A powerful laptop', category='Electronics', price=999.99,
                image_url='https://images.fonearena.com/blog/wp-content/uploads/2020/01/Falkon-Aerbook-MarQ-Flipkart-laptop.jpg', flipkart_url='https://www.flipkart.com/hp-pavilion-intel-core-i5-12th-gen-1235u-16-gb-512-gb-ssd-windows-11-home-14-dv2014tu-thin-light-laptop/p/itmb4b81cd1f873f?pid=COMGEG3ZNYZDAYVJ&lid=LSTCOMGEG3ZNYZDAYVJNYHV3Q'),
        Product(name='Smartphone', description='A high-end smartphone', category='Electronics', price=799.99,
                image_url='https://rukminim2.flixcart.com/image/850/1000/xif0q/mobile/m/e/8/-original-imagbwx4mqamdbzj.jpeg?q=90', flipkart_url='https://www.flipkart.com/redmi-note-11s-horizon-blue-64-gb/p/itm35daefaf408cb'),
        Product(name='Headphones', description='Noise-cancelling headphones', category='Electronics', price=199.99,
                image_url='https://rukminim1.flixcart.com/image/832/832/keq058w0-0/headphone/0/b/d/103-wireless-boat-original-imafvccxgjypzgew.jpeg?q=70', flipkart_url='https://www.flipkart.com/boat-103-wireless-bluetooth-headset/p/itmde6941010d8f1'),
        Product(name='Coffee Maker', description='Brews excellent coffee', category='Home Appliances', price=99.99,
                image_url='https://rukminim1.flixcart.com/image/1664/1664/coffee-maker/m/e/d/black-decker-dcm90-dcm90-original-imadsgkgvgbcc4gw.jpeg?q=90', flipkart_url='https://www.flipkart.com/black-decker-dcm90-12-cups-coffee-maker/p/itmdsfuzye9dzxd8'),
        Product(name='Vacuum Cleaner', description='A powerful vacuum cleaner', category='Home Appliances', price=149.99,
                image_url='https://rukminim1.flixcart.com/image/1664/1664/vacuum-cleaner/u/8/n/kent-cyclonic-original-imaeggcpdxdzdykw.jpeg?q=90', flipkart_url='https://www.flipkart.com/kent-kc-t3520-dry-vacuum-cleaner/p/itmegyqfhzqeghnz'),
        Product(name='Jewelry', description='Elegant gold necklace', category='Accessories', price=499.99,
                image_url='https://via.placeholder.com/150', flipkart_url='https://www.flipkart.com/gold-necklace'),
        Product(name='Pods', description='Wireless ear pods', category='Electronics', price=149.99,
                image_url='https://via.placeholder.com/150', flipkart_url='https://www.flipkart.com/wireless-ear-pods'),
        Product(name='Book', description='A fascinating novel', category='Books', price=19.99,
                image_url='https://via.placeholder.com/150', flipkart_url='https://www.flipkart.com/fascinating-novel'),
        Product(name='Clothes', description='Stylish denim jacket', category='Clothing', price=59.99,
                image_url='https://via.placeholder.com/150', flipkart_url='https://www.flipkart.com/stylish-denim-jacket')
    ]
    db.session.add_all(sample_products)
    db.session.commit()
    return 'Sample data added!'

if __name__ == '__main__':
    app.run(debug=True)
