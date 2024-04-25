import axios from "axios";
import React, { useEffect, useState } from "react";

function Coupon() {
  const [coupons, setCoupons] = useState([]);

  useEffect(() => {
    fetchCoupons();
  }, []);

  const fetchCoupons = async () => {
    try {
      const response = await axios.get("/api/v1/coupon/mycoupon/available", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });
      setCoupons(response.data);
    } catch (error) {
      console.error("Error fetching coupons:", error);
    }
  };

  return (
    <div>
      <h1>Coupon Page</h1>
      <div>
        {coupons.map((coupon_info) => (
          <div key={coupon_info.type}>
            <h2>{coupon_info.content}</h2>
            <p>{coupon_info.sale_price}</p>
            <p>Expires on: {coupon_info.duration}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Coupon;
