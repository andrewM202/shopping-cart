from flaskr.models import shopping_cart, db
import os
from flask import Flask, render_template, url_for, request, redirect
from flask_migrate import Migrate
import psycopg2
from sqlalchemy import create_engine

app = Flask(__name__)
# Figure out what this below does:
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# I am not entirely sure what track_mods does
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# create a Migrate object for migrations
migrate = Migrate(app, db)

db_string = os.environ.get('DATABASE_URL')
db = create_engine(db_string)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/add-to-cart', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        itemname = request.form['item-name']
        itemprice = request.form['item-price']
        
        db.execute(f"INSERT INTO shop_cart (item, price) VALUES ('{itemname}', '{itemprice}')")
        #db.session.add(new_item)
        #db.session.commit()
        return render_template('index.html')


@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    return render_template('checkout.html')


@app.route('/cart', methods=['POST', 'GET'])
def cart():
    items = db.execute("SELECT item FROM shop_cart")
    prices = db.execute("SELECT price FROM shop_cart")
    ids = db.execute("SELECT id FROM shop_cart")

    return render_template('cart.html', items=items, prices=prices, ids=ids)

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    print(id)
    item_to_delete = shopping_cart.query.get_or_404(id)
    db.execute(f"DELETE FROM shop_cart WHERE id='{id}'") 

    return redirect('/cart')

if __name__ == "__main__":
    app.run(debug=True)
