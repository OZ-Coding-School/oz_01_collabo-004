import axios from "axios";
import React, { useEffect, useState } from "react";
import "./Order.css";

const Order = () => {
  const [reservations, setReservations] = useState([]);

  useEffect(() => {
    fetchReservations();
  }, []);

  const fetchReservations = async () => {
    try {
      const response = await axios.get("API_ENDPOINT_HERE");
      setReservations(response.data);
    } catch (error) {
      console.error("Error fetching reservations:", error);
    }
  };

  return (
    <div>
      <div className="title">
        <h2>Dog</h2>
        <h2>Go</h2>
        <h2>와 함께 할 여행지</h2>
      </div>
      <div className="content"></div>
      <div className="order">
        <ul>
          {reservations.map((reservation) => (
            <li key={reservation.id}>
              {reservation.productName} - {reservation.date}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Order;
