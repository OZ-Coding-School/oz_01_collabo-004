import React from "react";
import "./Coupon.css";

function Coupon({ coupon, onReceiveCoupon }) {
  const handleReceiveCoupon = () => {
    onReceiveCoupon(coupon);
  };

  return (
    <div onClick={handleReceiveCoupon} className="coupon">
      <div className="coupon-image box">
        <h2>-₩50,000</h2>
        <h4>웰컴 쿠폰 받기</h4>
      </div>
      <div className="coupon-bottom box">
        <div className="dotted"></div>
        <p>할인 코드: DISCOUNT50</p>
        <p>유효 기간: 2024년 12월 31일까지</p>
      </div>
    </div>
  );
}

export default Coupon;
