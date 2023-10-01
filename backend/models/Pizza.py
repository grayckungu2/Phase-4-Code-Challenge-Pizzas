from models.dbconfig import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    
    # Define the relationship with RestaurantPizza
    restaurants = db.relationship('RestaurantPizza', back_populates='pizza')
