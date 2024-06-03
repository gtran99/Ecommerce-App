from flask import render_template, url_for, flash, redirect
from app import app, db
from app.models import User, Product
from app.forms import RegistrationForm, LoginForm

@app.route("/")
@app.route("/home")
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route("/products")
def products():
    all_products = Product.query.all()
    return render_template('products.html', products=all_products)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
