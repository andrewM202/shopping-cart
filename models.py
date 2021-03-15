from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class shopping_cart(db.Model):
    __tablename__ = 'shopping-cart'

    id = db.Column(db.BigInteger, primary_key = True)
    item = db.Column(db.String())
    price = db.Column(db.Numeric())

    def __init__(self, item, price):
        self.item = item
        sef.price = price

    def __repr__(self):
        return f"{self.item}:{self.price}"

    
