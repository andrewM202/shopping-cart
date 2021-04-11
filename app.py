from models import shopping_cart, db
import os
from flask import Flask, render_template, url_for, request, redirect
from flask_migrate import Migrate
import psycopg2

# creating the connection to the postgreSQL database
con = psycopg2.connect(database="shopping_cart", user="shopcart_user", password="", host="127.0.0.1")
cursor = con.cursor()

app = Flask(__name__)
# Figure out what this below does:
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# I am not entirely sure what track_mods does
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# create a Migrate object for migrations
migrate = Migrate(app, db)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/add-to-cart', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        item = request.form['item-name']
        price = request.form['item-price']
        
        new_item = shopping_cart(item=item, price=price)
        db.session.add(new_item)
        db.session.commit()
        return render_template('index.html')


@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    return render_template('checkout.html')


@app.route('/cart', methods=['POST', 'GET'])
def cart():
    cursor.execute("SELECT item FROM shop_cart;")
    items = cursor.fetchall()
    cursor.execute("SELECT price FROM shop_cart;")
    prices = cursor.fetchall()
    cursor.execute("SELECT id FROM shop_cart;")
    ids = cursor.fetchall()

    return render_template('cart.html', items=items, prices=prices, ids=ids)

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    item_to_delete = shopping_cart.query.get_or_404(id)
    db.session.delete(item_to_delete)
    db.session.commit()

    return redirect('/cart')

if __name__ == "__main__":
    app.run(debug=True)
