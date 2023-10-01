import React, { useState } from 'react';
import { Form, Button, Message } from 'semantic-ui-react'; // Import Semantic UI components
import { useForm } from 'react-hook-form';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const CreateRestaurantPizza = () => {
  const { register, handleSubmit, reset, formState: { errors } } = useForm();
  const [show, setShow] = useState(false);

  const createRestaurantPizza = async (data) => {
    console.log(data);

    const token = localStorage.getItem('REACT_TOKEN_AUTH_KEY');
    console.log(token);

    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${JSON.parse(token)}`
      },
      body: JSON.stringify(data)
    };

    try {
      const response = await fetch('http://localhost:5000/restaurant_pizzas', requestOptions);
      if (response.ok) {
        const responseData = await response.json();
        console.log('Restaurant Pizza created successfully:', responseData);
        reset();
        
        // Notify success here
        toast.success('Restaurant Pizza created successfully', {
          position: toast.POSITION.TOP_CENTER
        });
      } else {
        const errorData = await response.json();
        console.error('Error creating Restaurant Pizza:', errorData);
        
        // Notify error here
        toast.error(`Error creating Restaurant Pizza: ${errorData.error}`, {
          position: toast.POSITION.TOP_CENTER
        });
      }
    } catch (error) {
      console.error('Error creating Restaurant Pizza:', error);
      
      // Notify error here
      toast.error('Error creating Restaurant Pizza', {
        position: toast.POSITION.TOP_CENTER
      });
    }
  };

  return (
    <div className="container">
      <h1>Create a Restaurant Pizza</h1>
      <Form onSubmit={handleSubmit(createRestaurantPizza)}>
        <Form.Field>
          <label>Price</label>
          <input
            type="number"
            {...register('price', { required: true, min: 1, max: 30 })}
          />
        </Form.Field>
        {errors.price && (
          <Message negative>
            <p>Price is required and must be between 1 and 30</p>
          </Message>
        )}
        <Form.Field>
          <label>Pizza ID</label>
          <input
            type="number"
            {...register('pizza_id', { required: true })}
          />
        </Form.Field>
        {errors.pizza_id && (
          <Message negative>
            <p>Pizza ID is required</p>
          </Message>
        )}
        <Form.Field>
          <label>Restaurant ID</label>
          <input
            type="number"
            {...register('restaurant_id', { required: true })}
          />
        </Form.Field>
        {errors.restaurant_id && (
          <Message negative>
            <p>Restaurant ID is required</p>
          </Message>
        )}
        <Button primary type="submit">
          Create Restaurant Pizza
        </Button>
      </Form>

      {/* Toast container for notifications */}
      <ToastContainer />
    </div>
  );
};

export default CreateRestaurantPizza;
