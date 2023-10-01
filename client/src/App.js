import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'; // Import BrowserRouter and Link

import CreateRestaurantPizza from './components/CreateRestaurantPizza';
import PizzaList from './components/PizzaList';
import RestaurantList from './components/RestaurantList';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/pizzas">Pizza List</Link>
            </li>
            
            <li>
              <Link to="/create-restaurant-pizza">Create Restaurant Pizza</Link>
            </li>
            <li>
              <Link to="/">Restaurant List</Link>
            </li>
          </ul>
        </nav>

        <Route path="/pizzas" component={PizzaList} />
        <Route path="/create-restaurant-pizza" component={CreateRestaurantPizza} />
        <Route exact path="/" component={RestaurantList} /> {/* Use 'exact' to match the root path */}
      </div>
    </Router>
  );
}

export default App;
