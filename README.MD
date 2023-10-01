# Flask Code Challenge - Pizza Restaurants

This project is a Flask-based API for managing Pizza Restaurants. It includes models for `Restaurant`, `Pizza`, and `RestaurantPizza`, along with routes for various operations. Additionally, a React frontend application is provided to interact with the API.

## Requirements

- Python (3.6+)
- Flask
- SQLAlchemy
- React (for the frontend)
- Axios (for making HTTP requests in the frontend)

## Setup
the following steps are used for setting up this project 

### Backend (Flask API)

1. create a repository and Clone the Repository:
cd  to the  directory and the create folder Backend 


2. Create a Virtual Environment

   python -m venv venv
   source venv/bin/activate  

3. Install Dependencies:

 You can use `pip`, the Python package manager, to install Flask and its related packages all together using the following command:

```bash
pip install Flask Flask-Migrate Flask-SQLAlchemy Flask-Cors
``The above command will install the below packages `

- `Flask`: which is  Flask web framework.
- `Flask-Migrate`: A Flask extension for database migrations.
- `Flask-SQLAlchemy`: A Flask extension for interacting with SQL databases using SQLAlchemy.
- `Flask-Cors`: A Flask extension for handling Cross-Origin Resource Sharing (CORS) in  my application.

4. **Database Setup:**

   - Create a SQLite database for the project.
   - Update the `SQLALCHEMY_DATABASE_URI` in the `config.py` file with  database connection URL.

5. **Initialize the Database:**
cd to the backend directory 
   flask db init
   flask db migrate
   flask db upgrade
   Python seed.py

6. **Run the Flask API:**
   flask run
 The API  will be running at `http://127.0.0.1:5000`.

### Frontend (React Application)
back to the root directory  create react app by running (npx create-react-app client)

1. **Navigate to the client Directory:**

   cd client
   

2. **Install Dependencies:**

   npm install
   

3. **Start the React Application:**
   npm start
   ```

   The React application will start and run at `http://localhost:3000`.

## API Endpoints

### GET /restaurants

- Returns a JSON list of restaurants in the format:
  ```json
  [
    {
      "id": 1,
      "name": "Sottocasa NYC",
      "address": "298 Atlantic Ave, Brooklyn, NY 11201"
    },
    {
      "id": 2,
      "name": "PizzArte",
      "address": "69 W 55th St, New York, NY 10019"
    }
  ]
  ```

### GET /restaurants/:id

- If the restaurant exists, returns JSON data in the format:
  ```json
  {
    "id": 1,
    "name": "Sottocasa NYC",
    "address": "298 Atlantic Ave, Brooklyn, NY 11201",
    "pizzas": [
      {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
      }
    ]
  }
  ```
- If the restaurant does not exist, returns JSON data with an error message and the appropriate HTTP status code:
  ```json
  {
    "error": "Restaurant not found"
  }
  ```

### DELETE /restaurants/:id

- If the restaurant exists, it is removed from the database along with any associated `RestaurantPizza`s. Returns an empty response body and the appropriate HTTP status code.
- If the restaurant does not exist, returns JSON data with an error message and the appropriate HTTP status code:
  ```json
  {
    "error": "Restaurant not found"
  }
  ```

### GET /pizzas

- Returns a JSON list of pizzas in the format:
  ```json
  [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
  ```

### POST /restaurant_pizzas

- Creates a new `RestaurantPizza` associated with an existing `Pizza` and `Restaurant`. Accepts an object with the following properties in the request body:
  ```json
  {
    "price": 5,
    "pizza_id": 1,
    "restaurant_id": 3
  }
  ```
- If the `RestaurantPizza` is created successfully, it sends back a response with the data related to the `Pizza`:
  ```json
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  }
  ```
- If the `RestaurantPizza` is not created successfully (due to validation errors), returns JSON data with an error message and the appropriate HTTP status code:
  ```json
  {
    "errors": ["validation errors"]
  }
  ```

## Connecting React Frontend to Flask Backend
 Both the backend and frontend  should be running simultaneously for the full application to work correctly.

# Author 
Grace kungu