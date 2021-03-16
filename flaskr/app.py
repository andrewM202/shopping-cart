from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from flask_migrate import Migrate
from models import db, shopping_cart
 
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# I am not entirely sure what track_mods does
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:@localhost:5432/shopping_cart"

db.init_app(app)
# create a Migrate object for migrations
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-to-cart', methods=['POST'])
def form():
    if request.method == 'POST':
        item = request.form['item-name']
        price = request.form['item-price']
        new_item = shopping_cart(item=item, price=price)
        db.session.add(new_item)
        db.session.commit()
        return "Added it to cart successfully!"


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == "__main__":
    app.run(debug=True)
