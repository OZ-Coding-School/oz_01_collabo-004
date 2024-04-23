// Order.js
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useEffect, useState } from "react";
import axios from "../../api/axios";
import "./Order.css";

const Order = () => {
  const [orders, setOrders] = useState([]);
  const [filteredOrders, setFilteredOrders] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [completedOnly, setCompletedOnly] = useState(false);

  useEffect(() => {
    fetchOrders();
  }, []);

  useEffect(() => {
    filterOrders();
  }, [orders, searchTerm, completedOnly]);

  const fetchOrders = async () => {
    try {
      const response = await axios.get("/api/v1/order/", {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      });
      setOrders(response.data);
    } catch (error) {
      console.log("Error fetching orders:", error);
    }
  };

  const filterOrders = () => {
    let filtered = orders.filter((order) => {
      if (completedOnly && order.status !== "CANCEL") {
        return false;
      }
      if (
        searchTerm &&
        !order.product_info.name
          .toLowerCase()
          .includes(searchTerm.toLowerCase())
      ) {
        return false;
      }
      return true;
    });
    setFilteredOrders(filtered);
  };

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleCheckboxChange = (event) => {
    setCompletedOnly(event.target.checked);
  };

  const handleSearch = () => {
    filterOrders();
  };

  return (
    <div className="order-status">
      <div className="title">
        <h2>Dog</h2>
        <h2>Go</h2>
        <h2>와 함께 할 여행지</h2>
      </div>
      <div className="order-list">
        <h1>Order List</h1>
        <div className="filter-controls">
          <div className="search-input-container">
            <input
              type="text"
              placeholder="Search"
              value={searchTerm}
              onChange={handleSearchChange}
            />
            <button onClick={handleSearch}>
              <FontAwesomeIcon icon={faSearch} />
            </button>
          </div>
          <label>
            <input
              type="checkbox"
              checked={completedOnly}
              onChange={handleCheckboxChange}
            />
            예약 취소
          </label>
        </div>
        <div className="order-header">
          <div>Package Name</div>
          <div>Order Number</div>
          <div>Price</div>
          <div>Status</div>
          <div>Start Date</div>
          <div>End Date</div>
          <div>Coupon</div>
        </div>
        <ul className="order">
          {filteredOrders.map((order) => (
            <li key={order.order_id}>
              <div>{order.product_info.name}</div>

              <div>{order.total_price}</div>
              <div>{order.status}</div>
              <div>{order.departure_date}</div>
              <div>{order.return_date}</div>
              <div>{order.coupon.coupon_info.content}</div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Order;
