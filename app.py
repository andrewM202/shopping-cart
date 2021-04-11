from models import shopping_cart, db
import os
from flask import Flask, render_template, url_for, request, redirect
from flask_migrate import Migrate
import psycopg2

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 3000

# creating the connection to the postgreSQL database

app = Flask(__name__)
# Figure out what this below does:
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# I am not entirely sure what track_mods does
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# create a Migrate object for migrations
migrate = Migrate(app, db)

from sqlalchemy import create_engine
db_string = postgres://lefkbggqqoctza:f3efc8f36726f9fefd8cecd5bfb549e94162c08ca91326a330b065b018ebe6cc@ec2-34-225-103-117.compute-1.amazonaws.com:5432/d5jr1dkvvnk67r #"postgresql://andrewmatt:@localhost/shopping_cart"
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
