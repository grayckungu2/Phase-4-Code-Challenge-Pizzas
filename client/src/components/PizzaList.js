import React, { useEffect, useState } from 'react';
import { Button, Card, Modal } from 'react-bootstrap';

function PizzaList() {
  const [pizzas, setPizzas] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [selectedPizza, setSelectedPizza] = useState(null);

  useEffect(() => {
    const fetchPizzas = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/pizzas'); // Replace with your API endpoint
        if (response.ok) {
          const data = await response.json();
          setPizzas(data);
        } else {
          console.error('Error fetching pizzas:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching pizzas:', error);
      }
    };

    fetchPizzas();
  }, []);

  const handlePizzaClick = (pizza) => {
    setSelectedPizza(pizza);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setSelectedPizza(null);
    setShowModal(false);
  };

  return (
    <div>
      <h1>Pizza List</h1>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id} onClick={() => handlePizzaClick(pizza)}>
            {pizza.name} - {pizza.ingredients}
          </li>
        ))}
      </ul>

      {/* Pizza Modal */}
      <Modal show={showModal} onHide={handleCloseModal}>
        <Modal.Header closeButton>
          <Modal.Title>{selectedPizza?.name}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Card>
            <Card.Body>
              <Card.Title>{selectedPizza?.name}</Card.Title>
              <Card.Text>{selectedPizza?.ingredients}</Card.Text>
            </Card.Body>
          </Card>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleCloseModal}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default PizzaList;
