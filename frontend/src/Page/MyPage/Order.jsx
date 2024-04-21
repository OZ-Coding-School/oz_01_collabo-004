import React, { useEffect, useState } from "react";
import axios from "../../api/axios";
import "./Order.css";

const Order = () => {
  const [reservations, setReservations] = useState([]);

  useEffect(() => {
    fetchReservations();
  }, []);

  const fetchReservations = async () => {
    try {
      const response = await axios.get("/api/v1/order/", {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      });
      console.log(response.data);
      setReservations(response.data);
    } catch (error) {
      console.log("Error fetching reservations:", error);
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
