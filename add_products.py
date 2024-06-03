from app import app, db
from app.models import Product

with app.app_context():
    db.create_all()  # Ensure tables are created

    # Add some products without user_id
    product1 = Product(name='Product 1', description='Description of product 1', price=9.99)
    product2 = Product(name='Product 2', description='Description of product 2', price=19.99)
    product3 = Product(name='Product 3', description='Description of product 3', price=29.99)

    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.commit()

    print("Products added successfully!")
