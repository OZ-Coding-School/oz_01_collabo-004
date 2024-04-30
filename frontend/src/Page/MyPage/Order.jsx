import { faSearch } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../../api/axios";
import "./Order.css";
import ReviewModal from "./Review/ReviewModal";

const Order = ({ setCount }) => {
  const navigate = useNavigate();
  const [orders, setOrders] = useState([]);
  const [filteredOrders, setFilteredOrders] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [completedOnly, setCompletedOnly] = useState(false);
  const [paymentCompletedOnly, setPaymentCompletedOnly] = useState(false);
  const [cancelledOnly, setCancelledOnly] = useState(false);
  const [isReviewModalOpen, setIsReviewModalOpen] = useState(false);
  const [reviewOrderId, setReviewOrderId] = useState(null);
  const [productId, setProductId] = useState();

  useEffect(() => {
    fetchOrders();
  }, []);

  useEffect(() => {
    filterOrders();
  }, [orders, searchTerm, completedOnly, paymentCompletedOnly, cancelledOnly]);

  const fetchOrders = async () => {
    try {
      const response = await axios.get("/api/v1/order/", {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
      });
      setOrders(response.data);
      filterOrders();
    } catch (error) {}
  };

  const filterOrders = () => {
    let filtered = orders.filter((order) => {
      let includeOrder = true;

      if (
        completedOnly &&
        !paymentCompletedOnly &&
        order.status !== "ORDERED"
      ) {
        includeOrder = false;
      }
      if (!completedOnly && paymentCompletedOnly && order.status !== "PAID") {
        includeOrder = false;
      }
      if (cancelledOnly && order.status !== "CANCELLED") {
        includeOrder = false;
      }
      if (
        searchTerm &&
        !order.product_info.name
          .toLowerCase()
          .includes(searchTerm.toLowerCase())
      ) {
        includeOrder = false;
      }

      return includeOrder;
    });
    setFilteredOrders(filtered);
  };

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleCheckboxChange = (event) => {
    const { name, checked } = event.target;
    switch (name) {
      case "completedOnly":
        setCompletedOnly(checked);
        break;
      case "paymentCompletedOnly":
        setPaymentCompletedOnly(checked);
        break;
      case "cancelledOnly":
        setCancelledOnly(checked);
        break;
      default:
        break;
    }
  };

  const handleSearch = () => {
    filterOrders();
  };

  const handleReservationClick = (orderId) => {
    navigate(`/BookingPage/${orderId.product_info.id}`, {
      state: {
        id: orderId.order_id,
      },
    });
  };

  const handleReviewSubmit = (orderId) => {
    setIsReviewModalOpen(true);
    setReviewOrderId(orderId);
  };

  const handleReviewModalClose = () => {
    setIsReviewModalOpen(false);
    setReviewOrderId(null);
  };

  const handleOrderItemClick = (order) => {
    if (order.status === "ORDERED") {
      handleReservationClick(order);
    } else if (order.status === "PAID") {
      handleReviewSubmit(order.order_id);
    }
    setProductId(order.product_info.id);
  };

  return (
    <div className="order-status">
      <div className="title">
        <h2>Dog</h2>
        <h2>Go</h2>
        <h2>와 함께 할 여행지</h2>
      </div>
      <div className="order-list">
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
              name="completedOnly"
              checked={completedOnly}
              onChange={handleCheckboxChange}
            />
            예약 중
          </label>
          <label>
            <input
              type="checkbox"
              name="paymentCompletedOnly"
              checked={paymentCompletedOnly}
              onChange={handleCheckboxChange}
            />
            결제 완료
          </label>
          <label>
            <input
              type="checkbox"
              name="cancelledOnly"
              checked={cancelledOnly}
              onChange={handleCheckboxChange}
            />
            결제 취소
          </label>
        </div>
        <div className="order-header">
          <div>Package</div>
          <div>Price</div>
          <div>Status</div>
          <div>Start Date</div>
          <div>End Date</div>
          <div>Coupon</div>
          <div>Review</div>
        </div>
        <ul className="order">
          {filteredOrders.map((order) => (
            <li
              onClick={() => handleOrderItemClick(order)}
              key={order.order_id}
              className={order.status === "PAID" ? "paid" : ""}
            >
              <div>{order.product_info.name}</div>
              <div>{order.total_price}</div>
              <div>
                {order.status === "ORDERED"
                  ? "예약중"
                  : order.status === "PAID"
                  ? "결제완료"
                  : "결제 취소"}
              </div>
              <div>{order.departure_date}</div>
              <div>{order.return_date}</div>
              <div>{order.coupon ? order.coupon.coupon_info.content : ""}</div>
              <div>
                {order.status === "PAID" ? (
                  <span className="review_button">리뷰작성</span>
                ) : (
                  ""
                )}
              </div>
            </li>
          ))}
        </ul>
      </div>
      {isReviewModalOpen && (
        <ReviewModal
          setCount={setCount}
          productId={productId}
          orderId={reviewOrderId}
          onClose={handleReviewModalClose}
        />
      )}
    </div>
  );
};

export default Order;
