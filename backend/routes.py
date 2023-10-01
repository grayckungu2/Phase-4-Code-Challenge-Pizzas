from flask import Flask, make_response, jsonify, request, g

from flask_cors import CORS
from models.Restaurant import Restaurant
from models.Pizza import Pizza
from models.RestaurantPizza import RestaurantPizza
from sqlalchemy.exc import IntegrityError
import os
from models.dbconfig import db

def create_app():
    # Create the Flask app
    app = Flask(__name__)
    # Allow CORS for all routes
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)

    # Sample request hook
    @app.before_request
    def app_path():
        g.path = os.path.abspath(os.getcwd())

    @app.route('/', methods=['GET'])
    def index():
        response_body = 'Welcome to the Pizza Restaurants API'
        status_code = 200
        return make_response(response_body, status_code)

    # GET /restaurants
    @app.route('/restaurants', methods=['GET'])
    def get_restaurants():
        restaurants = Restaurant.query.all()
        restaurants_data = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants]
        return jsonify(restaurants_data)

    # GET /restaurants/:id
    @app.route('/restaurants/<int:id>', methods=['GET'])
    def get_restaurant_by_id(id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            restaurant_data = {"id": restaurant.id, "name": restaurant.name, "address": restaurant.address}
            return jsonify(restaurant_data)
        else:
            error_message = {"error": "Restaurant not found"}
            return jsonify(error_message), 404
    
    # DELETE /restaurants/:id
    @app.route('/restaurants/<int:id>', methods=['DELETE'])
    def delete_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            try:
                # Delete associated RestaurantPizza records first
                RestaurantPizza.query.filter_by(restaurant_id=id).delete()
                db.session.delete(restaurant)
                db.session.commit()
                return '', 204
            except IntegrityError as e:
                db.session.rollback()
                error_message = {"error": str(e)}
                return jsonify(error_message), 500
        else:
            error_message = {"error": "Restaurant not found"}
            return jsonify(error_message), 404

    # GET /pizzas
    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        pizzas = Pizza.query.all()
        pizzas_data = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
        return jsonify(pizzas_data)

    # POST /restaurant_pizzas
    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        try:
            data = request.get_json()
            price = int(data['price'])  # Convert 'price' to an integer

            if not (1 <= price <= 30):
                return jsonify({"error": "Price must be between 1 and 30"}), 400

            # Create the restaurant pizza with the validated 'price'
            restaurant_pizza = RestaurantPizza(
                price=price,
                pizza_id=data['pizza_id'],
                restaurant_id=data['restaurant_id']
            )

            # Add and commit the restaurant pizza to the database
            db.session.add(restaurant_pizza)
            db.session.commit()

            return jsonify({"message": "Restaurant Pizza created successfully"}), 201

        except ValueError:
            return jsonify({"error": "Invalid price format"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app
