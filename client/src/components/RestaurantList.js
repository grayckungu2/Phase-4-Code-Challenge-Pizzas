import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);
  const [searchId, setSearchId] = useState(''); // State to store the search ID

  useEffect(() => {
    fetchRestaurants();
  }, []);

  const fetchRestaurants = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/restaurants');
      if (response.ok) {
        const data = await response.json();
        setRestaurants(data);
      } else {
        console.error('Error fetching restaurant list:', response.statusText);
      }
    } catch (error) {
      console.error('Error fetching restaurant list:', error);
    }
  };

  const handleDeleteRestaurant = async (id) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/restaurants/${id}`, {
        method: 'DELETE',
      });

      if (response.ok) {
        // Restaurant deleted successfully, update the restaurant list
        fetchRestaurants();
      } else if (response.status === 404) {
        console.error('Restaurant not found');
      } else {
        console.error('Error deleting restaurant:', response.statusText);
      }
    } catch (error) {
      console.error('Error deleting restaurant:', error);
    }
  };

  const handleSearch = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/restaurants/${searchId}`);
      if (response.ok) {
        const data = await response.json();
        setRestaurants([data]); // Replace the restaurant list with the single result
      } else if (response.status === 404) {
        console.error('Restaurant not found');
        setRestaurants([]); // Clear the restaurant list
      } else {
        console.error('Error fetching restaurant by ID:', response.statusText);
      }
    } catch (error) {
      console.error('Error fetching restaurant by ID:', error);
    }
  };

  return (
    <div>
      <h1>Restaurant List</h1>
      <div>
        <label>Search by ID: </label>
        <input
          type="number"
          value={searchId}
          onChange={(e) => setSearchId(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}</Link>
            <button onClick={() => handleDeleteRestaurant(restaurant.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RestaurantList;
