# Import necessary modules 
from models.dbconfig import db
from faker import Faker
from flask_cors import CORS
from models.Restaurant import Restaurant
from models.Pizza import Pizza
from models.RestaurantPizza import RestaurantPizza
from sqlalchemy.exc import IntegrityError
from app import app
import random

# Initialize Faker with a specific seed 
fake = Faker()
Faker.seed(0)
# lists of realistic pizza names and ingredients
pizza_names = [
    "Margherita", "Pepperoni", "Supreme", "Hawaiian", "Vegetarian", "Mushroom Lovers",
    "BBQ Chicken", "Sausage and Peppers", "Four Cheese", "Pesto and Tomato", "Meat Lovers",
    "Buffalo Chicken", "Spinach and Artichoke", "Pineapple and Ham", "Bacon and Egg",
]

pizza_ingredients = [
    "Tomato Sauce", "Mozzarella Cheese", "Pepperoni", "Bell Peppers", "Onions",
    "Black Olives", "Sausage", "Bacon", "Mushrooms", "Pineapple", "Ham", "Chicken",
    "Spinach", "Artichoke Hearts", "Basil Pesto", "Tomatoes", "Garlic", "Oregano", "Parmesan Cheese",
]

# Function to create a new restaurant 
def create_new_restaurant_entry():
    name = fake.company()
    address = fake.address()
    return Restaurant(name=name, address=address)

# Function to create a new pizza 
def create_new_pizza_entry():
    name = random.choice(pizza_names) + " Pizza"
    ingredients = ", ".join(random.sample(pizza_ingredients, random.randint(3, 6)))
    return Pizza(name=name, ingredients=ingredients)

# Function to create a new restaurant_pizza with a random price
def create_new_restaurant_pizza_entry(restaurant, pizza):
    price = round(random.uniform(1, 30), 2)
    return RestaurantPizza(restaurant=restaurant, pizza=pizza, price=price)

# Function to seed the database
def seed_database():
    with app.app_context(): 
        for _ in range(15):
            restaurant = create_new_restaurant_entry()
            db.session.add(restaurant)

        for _ in range(15):
            pizza = create_new_pizza_entry()
            db.session.add(pizza)

        for _ in range(15):
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
