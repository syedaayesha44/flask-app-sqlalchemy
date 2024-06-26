from models import Product

def search_products(query):
    products = Product.query.filter(
        Product.name.ilike(f'%{query}%') |
        Product.description.ilike(f'%{query}%') |
        Product.category.ilike(f'%{query}%')
    ).all()
    return products
