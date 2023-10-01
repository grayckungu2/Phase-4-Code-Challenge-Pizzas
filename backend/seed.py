# Import necessary modules and set up your SQLAlchemy models
from models.dbconfig import db
from faker import Faker
from flask_cors import CORS
from models.Restaurant import Restaurant
from models.Pizza import Pizza
from models.RestaurantPizza import RestaurantPizza
from sqlalchemy.exc import IntegrityError
from app import app 
import random
 # Import your Flask app instance here

# Initialize Faker with a specific seed for consistent data generation
fake = Faker()
Faker.seed(0)

# Function to create a new restaurant with Faker-generated data
def create_new_restaurant_entry():
    name = fake.company()
    address = fake.address()
    return Restaurant(name=name, address=address)

# Function to create a new pizza with Faker-generated data
def create_new_pizza_entry():
    name = fake.word() + " Pizza"
    ingredients = ", ".join([fake.word() for _ in range(random.randint(3, 6))])
    return Pizza(name=name, ingredients=ingredients)

# Function to create a new restaurant_pizza with a random price
def create_new_restaurant_pizza_entry(restaurant, pizza):
    price = round(random.uniform(1, 30), 2)
    return RestaurantPizza(restaurant=restaurant, pizza=pizza, price=price)

# Function to seed the database
def seed_database():
    with app.app_context():  # Set up an application context
        for _ in range(10):
            restaurant = create_new_restaurant_entry()
            db.session.add(restaurant)

        for _ in range(10):
            pizza = create_new_pizza_entry()
            db.session.add(pizza)

        for _ in range(10):
            restaurant = random.choice(Restaurant.query.all())
            pizza = random.choice(Pizza.query.all())
            restaurant_pizza = create_new_restaurant_pizza_entry(restaurant, pizza)
            db.session.add(restaurant_pizza)

        try:
            db.session.commit()
            print("Database seeded successfully!")
        except IntegrityError as e:
            db.session.rollback()
            print(f"IntegrityError: {str(e)}")
            print("Rolling back changes to the database.")

if __name__ == '__main__':
    seed_database()
