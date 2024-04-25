import React, { useEffect, useState } from "react";
import axios from "../../api/axios";

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
      console.log(coupons);
    } catch (error) {
      console.error("Error fetching coupons:", error);
    }
  };

  return (
    <div>
      <h1>Coupon Page</h1>
      <div>
        {coupons.map((coupon, index) => (
          <div key={index}>
            <h2>{coupon.coupon_info.content}</h2>
            <p>{coupon.coupon_info.sale_price}</p>
            <p>{coupon.coupon_info.duration}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
export default Coupon;
