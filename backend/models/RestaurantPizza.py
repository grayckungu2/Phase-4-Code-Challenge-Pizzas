from models.dbconfig import db
from sqlalchemy.orm import validates
from models.dbconfig import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    
    #  foreign keys to link Restaurant and Pizza
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    
    #  relationship with Restaurant and Pizza
    restaurant = db.relationship('Restaurant', back_populates='pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurants')
    
    @validates('price')
    def validate_price(self, key, value):
        if not 1 <= value <= 30:
            raise ValueError("Price must be between 1 and 30.")
        return value


