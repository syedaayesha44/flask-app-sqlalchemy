from flask import Flask, render_template, request, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from models import db, Product, User, Recommendation, Image
from recommendations import get_recommendations, get_laptop_recommendations, collaborative_filtering_recommendations, get_smartphone_recommendations, get_vacuum_cleaner_recommendations,get_book, get_jwell, get_cloth, get_smartwatch, get_headfon
from search import search_products
from flask import flash
from werkzeug.utils import secure_filename
import os
from visual_search import perform_visual_search
from flask import Flask, render_template, request, redirect, url_for




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)
app.config['UPLOAD_FOLDER'] = 'uploaded_images'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/initialize-db')
def initialize_db():
    db.create_all()
    return 'Database initialized!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect('/')
        flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/')
def index():
    if not current_user.is_authenticated:
        return render_template('index.html')
    
    query = request.args.get('query')
    products = search_products(query) if query else Product.query.all()
    recommendations = []
    if current_user.is_authenticated:
        recommendations = collaborative_filtering_recommendations(current_user.id)
    return render_template('products.html', products=products, recommendations=recommendations)




@app.route('/uploaded_images/<filename>')
def uploaded_images(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)





@app.route('/visual_search')
def visual_search():
    return render_template('visual_search.html')

@app.route('/search_results', methods=['POST'])
def search_results():
    if 'image' in request.files:
        image = request.files['image']
        # Process the uploaded image and perform visual search
        search_results = perform_visual_search(image,app)
        
        # Pass the search results to the template and render it
        return render_template('search_results.html', results=search_results)
    
    return redirect(url_for('visual_search'))






    











# @app.route('/recommendations/<int:product_id>')
# @login_required
# def recommendations(product_id):
#     product = Product.query.get(product_id)
#     if not product:
#         return 'Product not found!', 404

#     products = Product.query.all()
#     recommendations = get_recommendations(product_id, [p.__dict__ for p in products])

#     # Determine the template and recommendation function based on the product category
#     if product.category.lower() == 'laptop':
#         recommendations = get_laptop_recommendations()
#         return render_template('laptop.html', product=product, recommendations=recommendations)
#     elif product.category.lower() == 'smartphone':
#         recommendations = get_smartphone_recommendations()
#         return render_template('smartphone.html', product=product, recommendations=recommendations)
#     # Add more categories as needed
#     else:
#         return render_template('recommendations.html', product=product, recommendations=recommendations)


@app.route('/recommendations/<int:product_id>')
@login_required
def recommendations(product_id):
    product = Product.query.get(product_id)
    if not product:
        return 'Product not found!', 404

    products = Product.query.all()
    recommendations = get_recommendations(product_id, [p.__dict__ for p in products])

    # Determine the template and recommendation function based on the product ID
    if product.id == 1:  # Assume 1 is the ID for laptops
        recommendations = get_laptop_recommendations(product_id)
        return render_template('laptop.html', product=product, recommendations=recommendations)
    elif product.id == 2:  # Assume 2 is the ID for smartphones
        recommendations = get_smartphone_recommendations(product_id)
        return render_template('smartphone.html', product=product, recommendations=recommendations)
    elif product.id == 4:  # Assume 2 is the ID for smartphones
        recommendations = get_vacuum_cleaner_recommendations(product_id)
        return render_template('vacum.html', product=product, recommendations=recommendations)
    elif product.id == 3:  # Assume 2 is the ID for smartphones
        recommendations = get_headfon(product_id)
        return render_template('head.html', product=product, recommendations=recommendations)
    elif product.id == 5:  # Assume 2 is the ID for smartphones
        recommendations = get_jwell(product_id)
        return render_template('jwell.html', product=product, recommendations=recommendations)
    elif product.id == 7:  # Assume 2 is the ID for smartphones
        recommendations = get_book(product_id)
        return render_template('book.html', product=product, recommendations=recommendations)
    elif product.id == 8:  # Assume 2 is the ID for smartphones
        recommendations = get_cloth(product_id)
        return render_template('cloth.html', product=product, recommendations=recommendations)
    # Add more product IDs as needed
    else:
        return render_template('recommendations.html', product=product, recommendations=recommendations)
















@app.route('/add-sample-data')
def add_sample_data():
    sample_products = [
        Product(name='Laptop', description='A powerful laptop', category='Electronics', price=999.99, image_url='https://example.com/laptop.jpg', flipkart_url='https://www.flipkart.com/laptop'),
        Product(name='Smartphone', description='A high-end smartphone', category='Electronics', price=799.99, image_url='https://example.com/smartphone.jpg', flipkart_url='https://www.flipkart.com/smartphone'),
        Product(name='Headphones', description='Noise-cancelling headphones', category='Electronics', price=199.99, image_url='https://example.com/headphones.jpg', flipkart_url='https://www.flipkart.com/headphones'),
        Product(name='Coffee Maker', description='Brews excellent coffee', category='Home Appliances', price=99.99, image_url='https://example.com/coffee_maker.jpg', flipkart_url='https://www.flipkart.com/coffee-maker'),
        Product(name='Vacuum Cleaner', description='A powerful vacuum cleaner', category='Home Appliances', price=149.99, image_url='https://example.com/vacuum_cleaner.jpg', flipkart_url='https://www.flipkart.com/vacuum-cleaner')
    ]
    db.session.add_all(sample_products)
    db.session.commit()
    return 'Sample data added!'

@app.route('/add-sample-recommendations')
def add_sample_recommendations():
    recommendations = [
        Recommendation(product_id=1, recommended_product_id=2),
        Recommendation(product_id=1, recommended_product_id=3),
        Recommendation(product_id=2, recommended_product_id=1),
        Recommendation(product_id=2, recommended_product_id=3),
        Recommendation(product_id=3, recommended_product_id=1),
        Recommendation(product_id=3, recommended_product_id=2),
    ]
    db.session.add_all(recommendations)
    db.session.commit()
    return 'Sample recommendations added!'

if __name__ == '__main__':
    app.run(debug=True)
